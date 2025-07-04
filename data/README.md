# Data Directory

This directory contains the datasets used for training and evaluating the BERT4Rec recommendation model.

## Required Datasets

### MovieLens Dataset
The model is designed to work with MovieLens datasets. Download the appropriate dataset:

**MovieLens 100K** (Recommended for quick testing):
```bash
wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
unzip ml-100k.zip -d data/
```

**MovieLens 1M** (For better performance):
```bash
wget http://files.grouplens.org/datasets/movielens/ml-1m.zip
unzip ml-1m.zip -d data/
```

**MovieLens 10M** (For large-scale experiments):
```bash
wget http://files.grouplens.org/datasets/movielens/ml-10m.zip
unzip ml-10m.zip -d data/
```

## Data Format

After downloading, your data directory should look like:
```
data/
├── ml-100k/
│   ├── u.data          # User ratings
│   ├── u.item          # Item information
│   ├── u.user          # User information
│   └── ...
├── ml-1m/
│   ├── ratings.dat     # User ratings
│   ├── movies.dat      # Movie information
│   ├── users.dat       # User information
│   └── ...
└── processed/          # Processed data (auto-generated)
    ├── train.txt
    ├── valid.txt
    └── test.txt
```

## Data Preprocessing

The raw data will be automatically preprocessed when you first run the model:

```python
from src.data_loader import DataLoader

# This will automatically download and preprocess the data
loader = DataLoader(dataset='ml-100k')
train_data, valid_data, test_data = loader.load_data()
```

## Custom Dataset

To use your own dataset, format it as a CSV file with columns:
- `user_id`: Unique user identifier
- `item_id`: Unique item identifier  
- `rating`: User rating for the item
- `timestamp`: Unix timestamp of the interaction

Example:
```csv
user_id,item_id,rating,timestamp
1,31,2.5,1260759144
1,1029,3.0,1260759179
1,1061,3.0,1260759182
```

Then place it in the `data/` directory and specify the path in your configuration.

## Data Statistics

### MovieLens 100K
- Users: 943
- Items: 1,682
- Ratings: 100,000
- Density: 6.30%

### MovieLens 1M
- Users: 6,040
- Items: 3,706
- Ratings: 1,000,209
- Density: 4.47%

## Configuration

Edit `config.py` to specify your dataset:

```python
# Dataset configuration
DATASET = 'ml-100k'  # or 'ml-1m', 'ml-10m', 'custom'
DATA_PATH = 'data/'
MIN_RATING = 4.0  # Minimum rating to consider as positive interaction
```