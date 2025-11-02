class RoomGridEnvironment:
    """
    6-room环境，管理状态、连接、奖励
    """
    def __init__(self, config):
        self.states = config['states']                    # ['A','B','C','D','E','F']
        self.adjacency = config['adjacency']              # dict of connections
        self.reward_matrix = config['reward_matrix']      # dict/array
        self.goal_state = config['goal_state']
        self.initial_state = config['initial_state']
        
    def get_legal_actions(self, state):
        """返回某状态的合法动作"""
        return self.adjacency.get(state, [])
    
    def get_reward(self, state, action):
        """获取转移奖励"""
        return self.reward_matrix.get((state, action), None)
    
    def step(self, state, action):
        """执行动作，返回(next_state, reward, done)"""
        
        # 第1步：先检查这个转移合不合法
        reward = self.get_reward(state, action)
        
        # 第2步：如果reward是None，说明这是非法转移
        if reward is None:
            return None, None, False  # ← 都返回None
        
        # 第3步：如果合法，才执行转移
        next_state = action
        done = (next_state == self.goal_state)
        return next_state, reward, done

    
    def reset(self):
        """重置到初始状态"""
        return self.initial_state
