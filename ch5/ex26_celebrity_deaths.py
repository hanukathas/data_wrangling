import pandas as pd
from pandas import DataFrame


def get_data():
    df = pd.read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/celebrity_deaths_4.csv',
                     usecols=['age', 'death_month', 'death_year'], encoding_errors="ignore", encoding="utf-8")

    return df


def selected_died_months(df: DataFrame):
    df2 = df.query('death_month in ("May", "June")')
    return df2


def remove_non_utf8(text):
    if isinstance(text, str):
        return text.encode('utf-8', errors='ignore').decode('utf-8')
    return text


if __name__ == '__main__':
    df = get_data()
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    df = df.loc[df['age'] < 100]
    print(df['age'].describe())

    df2 = selected_died_months(df)
    print(df2)
