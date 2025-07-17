import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)  # remove missing values
    df['date'] = pd.to_datetime(df['date'])
    return df