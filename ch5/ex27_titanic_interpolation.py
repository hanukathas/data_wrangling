import pandas as pd
from pandas import DataFrame


def get_data():
    df = pd.read_excel('/Users/karthikrajagopalan/git/data_wrangling/data/titanic3.xls')

    return df

def correct_age(df:DataFrame):
    df['age'] = df['age'].fillna(0)
    return df

def drop_fare_embarked(df: DataFrame):
    df = df.dropna(subset=['fare', 'embarked'])
    return df

def fix_home_dest(df: DataFrame):
    df['home.dest'] = df['home.dest'].fillna(df['home.dest'].mode()[0])
    return df.copy()


if __name__ == '__main__':
    df = get_data()
    print(df.columns[df.isnull().sum() > 0])
    print(df.isnull().sum())

    df2 = correct_age(df.copy())
    print(df2.isnull().sum())

    df3 = drop_fare_embarked(df2.copy())
    print(df3.isnull().sum())

    df4 = fix_home_dest(df3.copy())
    print(df4.isnull().sum())
