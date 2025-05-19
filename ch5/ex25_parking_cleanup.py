import pandas as pd
from pandas import DataFrame


def get_data():
    df = pd.read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/parking_violations.csv',
                     usecols=[ 'Plate ID', 'Registration State', 'Violation Time', 'Vehicle Make',
                              'Street Name', 'Vehicle Color'],
                     )
    return df

def drop_na(df: DataFrame) -> DataFrame:

    violation_count_na = len(df['Violation Time'])
    df = df.dropna()
    violation_count = len(df['Violation Time'])
    print(f"violation_count_na: {violation_count_na} | violation_count: {violation_count} | loss: {(violation_count_na - violation_count)*100:,}")
    return df

def na_selected_columns(df: DataFrame):
    # one method, not so readable
    decent_good_df = df[
        df['Plate ID'].notnull() &
        df['Registration State'].notnull() &
        df['Vehicle Make'].notnull() &
        df['Street Name'].notnull()
    ]
    # readable better
    decent_good_df_better = df.dropna(subset=['Plate ID', 'Registration State', 'Vehicle Make', 'Street Name'], thresh=3)

    non_na_len = len(decent_good_df.index)
    non_na_len_better = len(decent_good_df_better.index)

if __name__ == '__main__':
    df = get_data()
    df.info(show_counts=True)
    # print(f"is null sum")
    # print(df.isnull().sum())
    # df2 = drop_na(df)
    # df2.info(show_counts=True)

