from pandas import read_csv


def get_data():
    df = read_csv('/Users/karthikrajagopalan/git/data_wrangling/data/BTC-Hourly.csv')
    return df

def min_val():
    df = get_data()
    df_min = df.loc[
        df['close'] == df['close'].min(),
        ['date', 'close']
    ]
    return df_min

if __name__ == '__main__':
    print(min_val())