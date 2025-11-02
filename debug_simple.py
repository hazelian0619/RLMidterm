from config.defaults import CONFIG_BASELINE, CONFIG_MODIFIED
from core.environment import RoomGridEnvironment
from core.qlearner import QLearner


def debug_first_episode(config, num_steps=10):
    """只跑一个episode的前几步，看看发生了什么"""
    print(f"\n{'='*60}")
    print(f"Debugging: {config['name'].upper()}")
    print(f"Initial: {config['initial_state']} → Goal: {config['goal_state']}")
    print(f"{'='*60}\n")
    
    env = RoomGridEnvironment(config)
    learner = QLearner(config['states'], config['alpha'], config['gamma'], config['epsilon'])
    
    state = env.reset()
    episode_return = 0
    
    print(f"Start at: {state}\n")
    
    for step in range(num_steps):
        legal = env.get_legal_actions(state)
        action = learner.select_action(state, legal)
        next_state, reward, done = env.step(state, action)
        
        print(f"Step {step+1}: {state} → {next_state} | reward={reward:>3} | done={done}")
        
        episode_return += reward
        state = next_state
        
        if done:
            print(f"\n✓ Goal reached at step {step+1}!")
            break
    
    print(f"\nTotal return: {episode_return}")


if __name__ == '__main__':
    debug_first_episode(CONFIG_BASELINE, num_steps=5)
    debug_first_episode(CONFIG_MODIFIED, num_steps=10)
