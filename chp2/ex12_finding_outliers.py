import pandas as pd
from pandas import DataFrame


def get_data() -> DataFrame:
    df = pd.read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/trip_sample.csv').squeeze()
    df = df[['passenger_count', 'trip_distance']]
    return df

def get_total_passengers():
    df = get_data()
    return df['passenger_count'].iloc[:].sum()

def get_iqr():
    df = get_data()
    quantile_25 = df['trip_distance'].quantile(.25)
    quantile_75 = df['trip_distance'].quantile(.75)
    iqr = abs(quantile_75 - quantile_25)
    return iqr

def get_outliers(iqr) -> DataFrame:
    df = get_data()
    df = df[df['trip_distance'] < df['trip_distance'].quantile(0.75) + 1.5*iqr]
    print(df)
    return df

if __name__ == '__main__':
    # print(get_total_passengers())
    iqr = get_iqr()
    outliers = get_outliers(iqr)
    print(outliers)


