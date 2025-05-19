import numpy as np
import pandas as pd
from pandas import DataFrame


def get_data() -> DataFrame:
    df = pd.read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/trip_sample.csv',
                     usecols=['passenger_count','trip_distance','payment_type','total_amount'],
                     dtype={'passenger_count': np.int8, 'trip_distance': np.float16, 'payment_type': np.int8, 'total_amount': np.float16},
                     encoding_errors="",
                     keep_default_na=False,
                     skip_blank_lines = True,
                     comment='#'
                     )
    return df

def amount_paid_for_long_distances(df: DataFrame):
    return (df.sort_values('trip_distance', ascending=False)['total_amount']
            .head(5)
            .mean()
            )

def group_payment_type(df: DataFrame):
    """
    avg passenger count
    avg trip distance
    total amount paid
    :param df:
    :return:
    """
    return df.groupby('payment_type').agg(
        avg_passengers = ('passenger_count', 'mean'),
        avg_trip_distance = ('trip_distance', 'mean'),
        sum_amount = ('total_amount', 'sum')
    )


def amount_charged_by_riders(df: DataFrame):
    return (
        df.groupby('passenger_count')['total_amount']
        .agg(['sum', 'mean'])
        .round(0)
            )


def eight_passengers():
    df = get_data()
    count_passengers = df.loc[df['passenger_count'] > 3,'passenger_count'].count()
    return count_passengers

def zero_passengers():
    df = get_data()
    count_passengers = df.loc[df['passenger_count'] < 1,'passenger_count'].count()
    return count_passengers

def payment_over_1000():
    df = get_data()
    count_trips = df.loc[(df['total_amount'] > 10) & (df['payment_type'] == 1),'total_amount'].count()
    count_trips_query = df.query('total_amount > 10 and payment_type == 1')['passenger_count'].sum()
    return count_trips_query

def get_corr():
    df = get_data()
    return df.corr()

def sort_trip_distance(df: DataFrame):
    return df.groupby('payment_type')['total_amount'].mean().sort_values()

def label_distance_range(df: DataFrame):
    df['distance_range'] = pd.cut(df['passenger_count'],
                                  bins=[df['passenger_count'].min(), 2, 5, df['passenger_count'].max()],
                                  labels=['short', 'mid', 'long'],
                                  include_lowest= True)
    return df


if __name__ == '__main__':
    df = get_data()
    # print(amount_paid_for_long_distances(df))
    # print(amount_charged_by_riders(df))

    # df2 =  group_payment_type(df)
    # print(df2.rank(method="dense", na_option="bottom"))

    # print(sort_trip_distance(df))
    print(label_distance_range(df))
