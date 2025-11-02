CONFIG_BASELINE = {
    'name': 'baseline',
    'states': ['A', 'B', 'C', 'D', 'E', 'F'],
    'initial_state': 'B',
    'goal_state': 'F',
    'adjacency': {
        'A': ['E'],
        'B': ['D', 'F'],
        'C': ['D'],
        'D': ['B', 'C', 'E'],
        'E': ['A', 'D', 'F'],
        'F': ['B', 'E', 'F'] 
    },
    'reward_matrix': {
        ('A', 'E'): -1,
        ('B', 'D'): -1, ('B', 'F'): 50,
        ('C', 'D'): -1,
        ('D', 'B'): -1, ('D', 'C'): -1, ('D', 'E'): -1,
        ('E', 'A'): -1, ('E', 'D'): -1, ('E', 'F'): 50,
        ('F', 'B'): -1, ('F', 'E'): -1, ('F', 'F'): 50,
    },
    'alpha': 0.9,
    'gamma': 0.8,
    'epsilon': 0.1,
    'episodes': 500,
    'max_steps': 100,
}

CONFIG_MODIFIED = {
    'name': 'modified',
    'states': ['A', 'B', 'C', 'D', 'E', 'F'],
    'initial_state': 'A',
    'goal_state': 'C',
    'adjacency': CONFIG_BASELINE['adjacency'],
    'reward_matrix': {
        ('A', 'E'): -1,
        ('B', 'D'): -1,
        ('B', 'F'): -1,      # ← 改这里
        ('C', 'D'): -1,
        ('D', 'B'): -1,
        ('D', 'C'): 50,      # ← 新目标
        ('D', 'E'): -1,
        ('E', 'A'): -1,
        ('E', 'D'): -1,
        ('E', 'F'): -1,      # ← 改这里
        ('F', 'B'): -1,
        ('F', 'E'): -1,
        ('F', 'F'): -1,      # ← 改这里
        ('C', 'C'): 50,      # ← C的终点奖励
    },
    'alpha': 0.9,
    'gamma': 0.8,
    'epsilon': 0.1,
    'episodes': 500,
    'max_steps': 100,
}