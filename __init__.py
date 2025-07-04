"""
BERT4Rec: BERT-based Sequential Recommendation
=============================================

This module implements BERT4Rec, a sequential recommendation model based on 
the BERT (Bidirectional Encoder Representations from Transformers) architecture.

Key Components:
- BERT-based sequential recommendation model
- Masked language modeling for item sequences
- Attention mechanisms for capturing item relationships
- Data loaders for sequential recommendation datasets

Example Usage:
    from BERT4Rec import BERTModel, BERTTrainer
    
    # Initialize model and trainer
    model = BERTModel(config)
    trainer = BERTTrainer(model, config)
    
    # Train the model
    trainer.train()
"""

__version__ = "1.0.0"

try:
    from .models.bert import BERTModel
    from .trainers.bert import BERTTrainer
    from .dataloaders.bert import BertDataloader
    
    __all__ = [
        "BERTModel",
        "BERTTrainer",
        "BertDataloader"
    ]
    
except ImportError as e:
    print(f"Warning: Could not import BERT4Rec components: {e}")
    __all__ = []