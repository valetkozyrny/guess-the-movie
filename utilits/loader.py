import pandas as pd

def load_movies(csv_path):
    df = pd.read_csv(csv_path)
    df = df[['Movie Name', 'Description']].dropna()
    return df.to_dict(orient='records')