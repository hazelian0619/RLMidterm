# analysis/plotter.py
import matplotlib.pyplot as plt
import numpy as np


def plot_convergence(results, config_name, output_dir):
    """绘制收敛曲线"""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    # 图1：累积回报
    axes[0].plot(results['episode_returns'], linewidth=1.5, alpha=0.7)
    axes[0].set_xlabel('Episode')
    axes[0].set_ylabel('Cumulative Reward')
    axes[0].set_title(f'{config_name}: Episode Returns')
    axes[0].grid()
    
    # 图2：Q-table范数（收敛性指标）
    axes[1].plot(results['q_norms'], linewidth=1.5, alpha=0.7, color='orange')
    axes[1].set_xlabel('Episode')
    axes[1].set_ylabel('Q-table L1 Norm')
    axes[1].set_title(f'{config_name}: Q-value Convergence')
    axes[1].grid()
    
    plt.tight_layout()
    plt.savefig(output_dir / f'{config_name}_convergence.png', dpi=300)
    plt.close()


def plot_comparison(results_baseline, results_modified, output_path):
    """生成对比图（两条线在一张图上）"""
    
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    
    window = 50
    
    # Config 1
    r1 = results_baseline['episode_returns']
    ax.plot(r1, alpha=0.2, linewidth=0.8, color='#1f77b4')
    if len(r1) >= window:
        avg1 = np.convolve(r1, np.ones(window)/window, mode='valid')
        ax.plot(range(window-1, len(r1)), avg1, linewidth=2.5, 
                color='#1f77b4', label='Config 1: B→F')
    
    # Config 2
    r2 = results_modified['episode_returns']
    ax.plot(r2, alpha=0.2, linewidth=0.8, color='#ff7f0e')
    if len(r2) >= window:
        avg2 = np.convolve(r2, np.ones(window)/window, mode='valid')
        ax.plot(range(window-1, len(r2)), avg2, linewidth=2.5, 
                color='#ff7f0e', label='Config 2: A→C')
    
    ax.set_xlabel('Episode', fontsize=13)
    ax.set_ylabel('Cumulative Reward', fontsize=13)
    ax.set_title('Q-Learning Convergence Comparison', fontsize=14, fontweight='bold')
    ax.legend(loc='lower right', fontsize=11, framealpha=0.95)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"✓ Comparison plot saved to {output_path}")
