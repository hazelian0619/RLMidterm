# utils/logging.py
import json
import numpy as np


def save_results(output_dir, config, q_table, results):
    """保存训练结果到文件"""
    
    # 1. 保存Q-table
    q_table_txt = output_dir / 'q_table.txt'
    with open(q_table_txt, 'w') as f:
        f.write("Q-table entries (state, action) -> value\n")
        f.write("="*50 + "\n")
        for (s, a), v in sorted(q_table.items()):
            f.write(f"{s:>2} → {a:>2}: {v:>8.4f}\n")
    
    # 2. 保存episode_returns
    np.savetxt(
        output_dir / 'episode_returns.csv',
        results['episode_returns'],
        fmt='%.4f',
        delimiter=',',
        header='episode,return'
    )
    
    # 3. 保存q_norms
    np.savetxt(
        output_dir / 'q_norms.csv',
        results['q_norms'],
        fmt='%.4f',
        delimiter=',',
        header='episode,q_l1_norm'
    )
    
    # 4. 保存episode_steps
    np.savetxt(
        output_dir / 'episode_steps.csv',
        results['episode_steps'],
        fmt='%d',
        delimiter=',',
        header='episode,steps'
    )
    
    # 5. 保存配置
    config_json = output_dir / 'config.json'
    # 将reward_matrix中的元组键转换为字符串（JSON兼容）
    config_to_save = config.copy()
    config_to_save['reward_matrix'] = {
        f"{k[0]}->{k[1]}": v for k, v in config['reward_matrix'].items()
    }
    with open(config_json, 'w') as f:
        json.dump(config_to_save, f, indent=2)

    
    print(f"  Results saved:")
    print(f"    - q_table.txt")
    print(f"    - episode_returns.csv")
    print(f"    - q_norms.csv")
    print(f"    - episode_steps.csv")
    print(f"    - config.json")
