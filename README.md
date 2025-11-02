# Q-Learning Algorithm Implementation: Grid World Navigation

## 📖 Project Overview

This repository implements **tabular Q-Learning** for discrete room-based navigation, comparing convergence properties under two configurations as part of IOTA 5201 (RL for Intelligent Decision Making in CPS).

### Configurations
- **Config 1 (Baseline)**: Initial state B → Goal F (1-step optimal path)
  - Optimal return: 50
  - Convergence: ~50 episodes to 99.84% optimality
  
- **Config 2 (Modified)**: Initial state A → Goal C (3-step optimal path)
  - Optimal return: 48 
  - Convergence: ~100-150 episodes to 99.58% optimality

## 🔧 Requirements

- Python 3.7+
- numpy (numerical computation)
- matplotlib (visualization)
- pyyaml (configuration files)

## 📦 Installation

Clone repository
git clone https://github.com/hazelian0619/RLMidterm.git
cd RLMidterm

Install dependencies
pip install -r requirements.txt

text

## 🚀 Quick Start

Run both configurations
python main.py

Output files:
- baseline_convergence.png (Config 1 convergence)
- modified_convergence.png (Config 2 convergence)
- comparison.png (Side-by-side comparison)
- q_values_config1.txt (Final Q-table)
- q_values_config2.txt (Final Q-table)
text

## 📂 Project Structure

RLMidterm/
|
+-- core/                          # Core Q-Learning implementation
|   +-- __init__.py               # Package init
|   +-- environment.py            # Room-based grid environment
|   +-- qlearner.py               # Q-Learning agent
|
+-- config/                        # Configuration management
|   +-- __init__.py               # Package init
|   +-- defaults.py               # Hyperparameter defaults
|
+-- experiments/                   # Experiment runner
|   +-- configs/                  # Experiment configurations
|   |   +-- baseline.yaml         # Config 1 settings (B->F)
|   |   +-- modified.yaml         # Config 2 settings (A->C)
|   +-- __init__.py               # Package init
|   +-- runner.py                 # Training loop
|
+-- analysis/                      # Results analysis
|   +-- __init__.py               # Package init
|   +-- metrics.py                # Performance metrics calculation
|   +-- plotter.py                # Visualization utilities
|
+-- utils/                         # Utility functions
|   +-- __init__.py               # Package init
|   +-- logging.py                # Logging configuration
|
+-- main.py                        # Entry point script
+-- requirements.txt               # Python dependencies
+-- README.md                       # Project documentation
+-- report.pdf                      # Full analysis report


## 🧠 Algorithm: Q-Learning Update Rule

Q(s,a) ← Q(s,a) + α[r + γ·max_a' Q(s',a') - Q(s,a)]

text

Where:
- `α = 0.9` : Learning rate
- `γ = 0.8` : Discount factor  
- `ε = 0.1` : Exploration rate (ε-greedy)

## 📊 Key Results

| Metric | Config 1 | Config 2 | Ratio |
|--------|----------|----------|-------|
| Episodes to convergence | 50 | 100-150 | 2-3× |
| Mean return (final 100) | 49.92 | 47.80 | -2.12 |
| Optimality | 99.84% | 99.58% | ~equal |
| Path length | 1 step | 3 steps | 3× |
| Q-norm final | 170.34 | 320.90 | 1.88× |

## 🔬 Experimental Design

### Configuration 1: Baseline (B→F)
Shortest path with direct connection
Initial state: B
Goal state: F
Reward structure: R(B,F)=50, R(E,F)=50, all other transitions=-1

text

### Configuration 2: Modified (A→C)
Longer path requiring goal reorientation
Initial state: A
Goal state: C
Reward structure: R(D,C)=50, R(C,C)=50
Old goal: R(B,F)=R(E,F)=R(F,F)=-1 (unlearning)
Optimal path: A → E → D → C

text

## 📈 Generated Outputs

After running `main.py`, you will get:

1. **baseline_convergence.png** - Config 1 training curves
   - Left: Episode returns over time
   - Right: Q-table L1 norm convergence

2. **modified_convergence.png** - Config 2 training curves
   - Shows slower convergence due to 3-step path

3. **comparison.png** - Direct convergence comparison
   - Blue: Config 1 (rapid convergence)
   - Orange: Config 2 (slower convergence)

4. **Q-value files** - Final learned Q-values for analysis

## 💡 Key Insights

1. **Convergence Scaling**: Training time scales ~linearly with path complexity (2-3× for 3× path increase)

2. **Optimality Robustness**: Both configurations achieve >99% optimality despite different complexity levels

3. **Exploration Efficiency**: Config 2 has lower per-episode deficits (0.0013 vs 0.0016) despite longer paths

4. **Hyperparameter Transferability**: Choices (α=0.9, γ=0.8, ε=0.1) work well for both tasks

## 📄 Report

See `report.pdf` for complete analysis including:
- Theoretical background and significance
- Environment and reward structure details
- Initial/goal state change impact analysis
- Convergence behavior analysis
- Theoretical validation and CPS applications

## 🤝 Author

**Lian Wanchen**  
Information & Artificial Intelligence Track  
The Hong Kong University of Science and Technology (Guangzhou)  
Student ID: 50018021

## 📚 References

- Watkins, C. J., & Dayan, P. (1992). Q-learning. Machine Learning, 8(3-4), 279-292.
- Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction.
