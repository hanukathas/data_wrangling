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


if __name__ == '__main__':
    print(payment_over_1000())
