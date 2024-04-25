import argparse
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
from loguru import logger

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', required=True, type=str, help='a csv file with input data (no targets)')
parser.add_argument('--predictions_file', required=True, type=str, help='a csv file where predictions will be saved to')
parser.add_argument('--model_file', required=True, type=str, help='a pkl file with a model already stored (see train.py)')

args = parser.parse_args()

model_file = args.model_file
input_file = args.input_file
predictions_file = args.predictions_file

if not os.path.isfile(model_file):
    logger.error(f"model file {model_file} does not exist")
    exit(-1)

if not os.path.isfile(input_file):
    logger.error(f"input file {input_file} does not exist")
    exit(-1)

logger.info("loading input data")
Xts = pd.read_csv(input_file).values[:,:2]

logger.info("loading model")
with open(model_file, 'rb') as f:
    m = pickle.load(f)

logger.info("making predictions")
preds = m.predict(Xts)

logger.info(f"saving predictions to {predictions_file}")
pd.DataFrame(preds, columns=['preds']).to_csv(predictions_file, index=False)
