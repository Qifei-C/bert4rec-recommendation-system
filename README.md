# BERT4Rec: Sequential Recommendation with BERT

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-red.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

State-of-the-art sequential recommendation system using BERT (Bidirectional Encoder Representations from Transformers) architecture. BERT4Rec captures complex sequential patterns in user behavior to provide highly accurate next-item recommendations.

## 🎯 Features

- **BERT Architecture**: Bidirectional transformer for sequential modeling
- **Masked Language Modeling**: Learns from user interaction sequences
- **Self-Attention**: Captures long-range dependencies in user behavior
- **Scalable Training**: Efficient implementation for large datasets
- **State-of-the-Art Results**: Superior performance on benchmark datasets

## 🚀 Quick Start

```python
from src.bert4rec import BERT4Rec, SequentialDataset

# Initialize model
model = BERT4Rec(
    vocab_size=10000,
    hidden_size=256,
    num_layers=6,
    num_heads=8,
    max_seq_length=50
)

# Prepare sequential data
dataset = SequentialDataset(
    user_sequences=user_sequences,
    max_length=50,
    mask_prob=0.15
)

# Train model
trainer = BERT4RecTrainer(model, dataset)
trainer.train(epochs=100, batch_size=256)

# Generate recommendations
recommendations = model.recommend(user_sequence, top_k=10)
```

## 🏗 Architecture

### BERT4Rec Components

1. **Item Embedding Layer**
   - Maps items to dense vectors
   - Learnable position embeddings
   - Segment embeddings for sequence structure

2. **Multi-Head Self-Attention**
   - Bidirectional attention mechanism
   - Captures item-item relationships
   - Multiple attention heads for different patterns

3. **Feed-Forward Networks**
   - Point-wise transformations
   - Non-linear activation functions
   - Residual connections and layer normalization

4. **Masked Language Modeling**
   - Randomly masks items in sequences
   - Predicts masked items using context
   - Learns rich item representations

## 📊 Performance Benchmarks

Performance will vary based on your dataset characteristics and hardware configuration. The BERT architecture is designed to achieve competitive results on sequential recommendation tasks.

## 📁 Project Structure

```
bert4rec-recommendation-system/
├── src/                     # Source code
│   ├── bert4rec.py         # Main BERT4Rec model
│   ├── trainer.py          # Training utilities
│   └── dataset.py          # Data preprocessing
├── examples/               # Example scripts
├── tests/                  # Test suite
├── docs/                   # Documentation
├── data/                   # Data directory
├── models/                 # Pre-trained models
└── README.md              # This file
```

## 🔧 Advanced Features

### Custom Attention Patterns
```python
# Configure attention mechanism
model = BERT4Rec(
    attention_type='scaled_dot_product',
    dropout_rate=0.1,
    attention_dropout=0.1
)
```

### Transfer Learning
```python
# Load pre-trained weights
model.load_pretrained('models/bert4rec_pretrained.pt')

# Fine-tune on your dataset
model.fine_tune(target_dataset, epochs=20)
```

## 📈 Research Applications

This implementation supports research in:
- Sequential recommendation systems
- Transformer architectures for RecSys
- Self-supervised learning in recommendations
- Long-term user behavior modeling

## 🤝 Contributing

We welcome contributions to improve BERT4Rec! Please submit issues and pull requests.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 📚 Citation

```bibtex
@article{sun2019bert4rec,
  title={BERT4Rec: Sequential recommendation with bidirectional encoder representations from transformer},
  author={Sun, Fei and Liu, Jun and Wu, Jian and Pei, Changhua and Lin, Xiao and Ou, Wenwu and Jiang, Peng},
  journal={CIKM},
  year={2019}
}
```

---

🔍 **Sequential Recommendations with Transformer Power**