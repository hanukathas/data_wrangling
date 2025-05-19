import pandas as pd
from pandas import DataFrame


def get_data() -> DataFrame:
    df = pd.read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/NYC_Weather_2016_2022.csv')
    df = df[['time', 'temp']]
    return df

def get_hour() -> DataFrame:
    df_data = get_data()
    df_time = pd.to_datetime(df_data['time'])
    df_time.columns = 'hour'
    print(df_time.hour)
    # df = pd.concat([df_data['time'].dt.hour, df_data['temp']])
    # return df

def replace_temp_less_than_0():
    df_data = get_data()
    df_data.loc[
        df_data['temp'] < 0.0,
        'temp'
    ] = 0
    return df_data

def replace_nan():
    df_data = get_data()
    df_replaced_nan = df_data.fillna(0)
    return df_replaced_nan

if __name__ == '__main__':
    print(replace_nan())



