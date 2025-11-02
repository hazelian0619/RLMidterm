import numpy as np

class QLearner:
    """
    标准Q-learning，与环境解耦
    """
    def __init__(self, states, alpha, gamma, epsilon):
        self.states = states
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.Q = {(s, a): 0.0 for s in states for a in states}  # 初始化
        
    def select_action(self, state, legal_actions):
        """ε-greedy 选择"""
        if np.random.rand() < self.epsilon:
            # 探索：随机选择
            return np.random.choice(legal_actions)
        else:
            # 利用：选最大Q值的动作
            q_vals = [self.Q.get((state, a), -np.inf) for a in legal_actions]
            
            # 找到最大Q值
            max_q = max(q_vals)
            
            # 如果多个动作都有相同的最大Q值，随机选一个
            # （这样在初期Q都是0时，也能随机选）
            best_actions = [a for a, q in zip(legal_actions, q_vals) if q == max_q]
            return np.random.choice(best_actions)

    
    def update(self, state, action, reward, next_state, legal_next_actions):
        """Q-learning更新规则"""
        if legal_next_actions:
            max_q_next = max([self.Q.get((next_state, a), -np.inf) 
                             for a in legal_next_actions])
        else:
            max_q_next = 0
        
        td_error = reward + self.gamma * max_q_next - self.Q[(state, action)]
        self.Q[(state, action)] += self.alpha * td_error
    
    def get_q_table_norm(self):
        """收敛性指标：Q-table L1范数"""
        return sum(abs(v) for v in self.Q.values())

    def train(self, env, num_episodes, max_steps):
        """
        完整训练流程
        返回：(final_Q, episode_returns, convergence_history)
        """
        episode_returns = []
        convergence_history = []
        
        for episode in range(num_episodes):
            state = env.reset()
            episode_return = 0
            
            for step in range(max_steps):
                # 获取合法动作
                legal_actions = env.get_legal_actions(state)
                
                # ε-greedy选动作
                action = self.select_action(state, legal_actions)
                
                # 环境执行
                next_state, reward, done = env.step(state, action)
                
                # 获取下一状态的合法动作
                legal_next_actions = env.get_legal_actions(next_state)
                
                # Q-learning更新
                self.update(state, action, reward, next_state, legal_next_actions)
                
                # 累计回报
                episode_return += reward
                state = next_state
                
                if done:
                    break
            
            # 记录
            episode_returns.append(episode_return)
            convergence_history.append(self.get_q_table_norm())
        
        return self.Q, episode_returns, convergence_history
