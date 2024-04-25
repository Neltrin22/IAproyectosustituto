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
parser.add_argument('--data_file', required=True, type=str, help='a csv file with train data')
parser.add_argument('--model_file', required=True, type=str, help='where the trained model will be stored')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='if sets overwrites the model file if it exists')

args = parser.parse_args()

model_file = args.model_file
data_file = args.data_file
overwrite = args.overwrite_model

if os.path.isfile(model_file):
    if overwrite:
        logger.info(f"overwriting existing model file {model_file}")
    else:
        logger.info(f"model file {model_file} exists. exiting. use --overwrite_model option")
        exit(-1)

logger.info("loading train data")
data = pd.read_csv(data_file)

# Separate features and target variable
X = data.drop(columns=["id", "NObeyesdad"])
y = data["NObeyesdad"]

# One-hot encode categorical features
X_encoded = pd.get_dummies(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Define the classifier
rf = RandomForestClassifier(random_state=42)

# Define the hyperparameters to tune
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Perform grid search cross-validation
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Get the best model
best_rf = grid_search.best_estimator_

# Evaluate the best model
best_rf_pred = best_rf.predict(X_test)
best_accuracy = accuracy_score(y_test, best_rf_pred)
print("Best Model Accuracy:", best_accuracy)

# Save the best model
logger.info(f"saving model to {model_file}")
with open(model_file, "wb") as f:
    pickle.dump(best_rf, f)
