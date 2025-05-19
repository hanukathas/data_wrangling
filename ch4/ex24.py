import pandas as pd
from pandas import DataFrame

'''
Summons Number,Plate ID,Registration State,Plate Type,Issue Date,Violation Code,Vehicle Body Type,Vehicle Make,Issuing Agency,Street Code1,Street Code2,Street Code3,Vehicle Expiration Date,Violation Location,Violation Precinct,Issuer Precinct,Issuer Code,Issuer Command,Issuer Squad,Violation Time,Time First Observed,Violation County,Violation In Front Of Or Opposite,House Number,Street Name,Intersecting Street,Date First Observed,Law Section,Sub Division,Violation Legal Code,Days Parking In Effect    ,From Hours In Effect,To Hours In Effect,Vehicle Color,Unregistered Vehicle?,Vehicle Year,Meter Number,Feet From Curb,Violation Post Code,Violation Description,No Standing or Stopping Violation,Hydrant Violation,Double Parking Violation,Latitude,Longitude,Community Board,Community Council ,Census Tract,BIN,BBL,NTA
'''


def get_data():
    df = pd.read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/parking_violations.csv',
                     usecols=['Date First Observed', 'Plate ID', 'Registration State', 'Issue Date', 'Vehicle Make',
                              'Street Name', 'Vehicle Color'],
                     )
    df.set_index('Issue Date', inplace=True)
    return df


def count_three_most_common_vehicles(df: DataFrame):
    return df.loc['08/05/2013', 'Vehicle Make'].value_counts().head(3)


def count_three_most_ticketed_vehicles(df: DataFrame):
    df['year'] = pd.to_datetime(df.index)
    df['month'] = pd.to_datetime(df.index)
    df['day'] = pd.to_datetime(df.index)
    df['year'] = df['year'].dt.year
    df['month'] = df['month'].dt.month
    df['day'] = df['day'].dt.day

    df_day = df.loc[(df['day'] > 2), 'Vehicle Make'].value_counts()
    df_year = df.loc[(df['year'] == 2013), 'Vehicle Make'].value_counts()
    df_month = df.loc[(df['month'] == 8) & (df['year'] == 2013) & (df['day'] > 2) & (
                df['day'] < 9), 'Vehicle Make'].value_counts().head(2)

    return df_month[1]


def count_vehicle_make_by_color(df: DataFrame):
    # df2 = df['Vehicle Color'].fillna('GOLD')

    df.set_index('Vehicle Color', inplace=True)
    return df.loc[['BLUE', 'RED'], 'Vehicle Make'].value_counts().head(3)

    # return df.loc[['BLUE', 'RED'], 'Vehicle Make'].value_counts()

def sort_by_index(df: DataFrame):
    return df.sort_index()


if __name__ == '__main__':
    df = get_data()
    # print(count_three_most_common_vehicles(df))
    # print(count_vehicle_make_by_color(df))
    # print(count_three_most_ticketed_vehicles(df))
    print(sort_by_index(df))
