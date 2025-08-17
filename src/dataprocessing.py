import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    # Rename and select necessary columns
    df = df[['Order Date', 'Total Revenue']]
    df = df.rename(columns={'Order Date': 'ds', 'Total Revenue': 'y'})

    # Convert dates to datetime
    df['ds'] = pd.to_datetime(df['ds'], errors='coerce')

    # Drop rows with invalid dates or missing values
    df = df.dropna(subset=['ds', 'y'])

    # Optional: Aggregate by month if there are multiple entries per date
    df = df.groupby('ds').sum().reset_index()

    return df
