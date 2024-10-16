# src/model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier       # Can use either of the classifiers(RandomForestClassifier/XGBClassifier) for model training      
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, f1_score

def load_processed_data(filepath):
    """
    Load the processed dataset into a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def define_features_target(df):
    """
    Define input features and target variable.
    """
    x = df.drop(['churn', 'customer_id','age_group'], axis=1)  # Assuming 'churn' is the target
    y = df['churn']
    return x, y

def train_model(x_train, y_train):
    """
    TOD: Train a model using either RandomForestClassifier or XGBClassifier. Comment out the model to be used
    """
    # model = RandomForestClassifier(n_estimators=100, random_state=42)
    # model.fit(x_train, y_train)
    
    # TOD: Train the XGBClassifier model
    model = XGBClassifier(use_label_encoder = True, eval_metric='logloss', enable_categorical=True)
    model.fit(x_train, y_train)
    
    return model


def evaluate_model(model, x_test, y_test):
    """
    Evaluate the model using Accuracy and F1 Score.
    """
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    print(f"F1 Score: {f1:.4f}")
    
    return accuracy, f1

def main():
    # Load processed data
    df = load_processed_data('data/processed_bank_churn.csv')
    
    # Define features and target
    x, y = define_features_target(df)
    
    # Split into training and testing sets
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    # Train model
    model = train_model(x_train, y_train)
    
    # Evaluate model
    evaluate_model(model, x_test, y_test)

if __name__ == "__main__":
    main()
