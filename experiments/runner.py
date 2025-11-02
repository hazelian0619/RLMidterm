import numpy as np
from pathlib import Path
from core.environment import RoomGridEnvironment
from core.qlearner import QLearner
from utils.logging import save_results

class ExperimentRunner:
    def __init__(self, config):
        self.config = config
        self.env = RoomGridEnvironment(config)
        self.learner = QLearner(
            config['states'],
            config['alpha'],
            config['gamma'],
            config['epsilon']
        )
        self.results = {
            'episode_returns': [],
            'q_norms': [],
            'episode_steps': []
        }
    
    def train(self):
        """主训练循环"""
        for episode in range(self.config['episodes']):
            state = self.env.reset()
            episode_return = 0
            steps = 0
            
            for step in range(self.config['max_steps']):
                legal_actions = self.env.get_legal_actions(state)
                action = self.learner.select_action(state, legal_actions)
                
                next_state, reward, done = self.env.step(state, action)
                legal_next_actions = self.env.get_legal_actions(next_state)
                
                self.learner.update(state, action, reward, next_state, legal_next_actions)
                
                episode_return += reward
                steps += 1
                state = next_state
                
                if done:
                    break
            
            self.results['episode_returns'].append(episode_return)
            self.results['q_norms'].append(self.learner.get_q_table_norm())
            self.results['episode_steps'].append(steps)
            
            if (episode + 1) % 100 == 0:
                print(f"Episode {episode+1}/{self.config['episodes']}, Return: {episode_return}")
        
        return self.learner.Q, self.results
    
    def save(self, output_dir):
        """保存结果与配置"""
        save_results(output_dir, self.config, self.learner.Q, self.results)
