
import pandas as pd

def load_data(filepath):
    """
    Load the dataset into a pandas DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def check_missing_values(df):
    
    missing = df.isnull().sum()

    print("Missing Values:\n", missing)

def generate_summary_statistics(df):
    summary = df.describe()
    print("Summary Statistics:\n", summary)

def main():
    # Load data
    df = load_data('data/bank_churn.csv')
    
    check_missing_values(df) #T : Check for missing values by calling it's function
    
    generate_summary_statistics(df) # TOO : Generate summary statistics by calling it's function

if __name__ == "__main__":
    main()


