# BERT4Rec: Sequential Recommendation with BERT

This repository implements the BERT4Rec model for sequential recommendation, as described in the paper "BERT4Rec: Sequential Recommendation with BERT" (Sun et al.).

## 🚀 Core Components

*   **BERT4Rec Model**: Implementation of the BERT-based architecture for sequential recommendation.
*   **Dataloaders**: Utilities for processing and loading sequential data for the model.
*   **Trainers**: Scripts for training the BERT4Rec model.

## 🎯 Project Objective

The main objective of this project is to provide a functional implementation of BERT4Rec, allowing for training and evaluation on datasets like MovieLens-1m and MovieLens-20m.

## 🛠️ Usage

To use this project, you can run the `main.py` script with the appropriate template to train and/or test the BERT4Rec model.

### Training BERT4Rec

```bash
python main.py --template train_bert
```

## 📁 Project Structure

```
BERT4Rec/
├── config.py                # Configuration settings for the model
├── dataloaders/             # Data loading and preprocessing utilities
├── datasets/                # Dataset-related utilities
├── Images/                  # Images used in the README
├── LICENSE                  # Project license file
├── loggers.py               # Logging utilities
├── main.py                  # Main script to run training and testing
├── models/                  # Model architectures
├── options.py               # Command-line options parser
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── templates.py             # Predefined templates for running models
├── trainers/                # Training utilities
└── utils.py                 # General utility functions
```