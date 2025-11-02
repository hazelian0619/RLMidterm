from pathlib import Path
import shutil             
from config.defaults import CONFIG_BASELINE, CONFIG_MODIFIED
from experiments.runner import ExperimentRunner
from analysis.plotter import plot_convergence

def main():
    results_dir = Path('results')
    all_results = {}  # ← 新增：保存所有结果
    
    for config in [CONFIG_BASELINE, CONFIG_MODIFIED]:
        print(f"\n{'='*60}")
        print(f"Running: {config['name'].upper()}")
        print(f"{'='*60}")
        
        config_dir = results_dir / config['name']
        if config_dir.exists():
            shutil.rmtree(config_dir)
        config_dir.mkdir(parents=True, exist_ok=True)
        
        runner = ExperimentRunner(config)
        q_table, results = runner.train()
        runner.save(config_dir)
        plot_convergence(results, config['name'], config_dir)
        
        all_results[config['name']] = results  # ← 新增：保存
        
        print(f"\n✓ Results saved to {config_dir}")
    
    # ← 新增：生成对比图
    from analysis.plotter import plot_comparison
    plot_comparison(
        all_results['baseline'], 
        all_results['modified'], 
        results_dir / 'comparison.png'
    )
    
    print(f"\n{'='*60}")
    print("✓ ALL DONE!")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
