import pandas as pd
from pandas import DataFrame

pd.set_eng_float_format(3)


def build_data() -> DataFrame:
    data_list = [[12, "cap", 100, 120, 500],
                 [14, "latte", 150, 250, 50],
                 [15, "ame", 120, 140, 90],
                 [16, "exp", 80, 100, 5000],
                 [17, "milk", 40, 60, 6500]]

    df = pd.DataFrame(data=data_list, columns=['id', 'product', 'wp', 'rp', 'sold'])

    return df


def sum_sales():
    df = build_data()
    df['sum'] = df['rp'] * df['sold']
    return sum(df['sum'])


def get_higher_priced():
    df = build_data()
    df['higher_price'] = (df['rp'] - df['wp']) >= 50
    return df


if __name__ == '__main__':
    print(get_higher_priced())
