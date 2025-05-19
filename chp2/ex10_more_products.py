import pandas as pd
from pandas import DataFrame


def build_data() -> DataFrame:
    data_list = [[12, "cap", 100, 120, 500],
                 [14, "latte", 150, 250, 50],
                 [15, "ame", 120, 140, 90],
                 [19, "exp", 80, 100, 5000],
                 [20, "milk", 40, 60, 6500]]

    df = pd.DataFrame(data=data_list, columns=['id', 'product', 'wp', 'rp', 'sold'])

    return df

def add_items() -> DataFrame:
    df = build_data()
    data_list = [[24, "phone", 200, 500, 0],
                 [16, "apple", 0.5, 1, 0],
                 [17, "pear", 0.6, 1.2, 0]]
    df2 = pd.DataFrame(data=data_list, columns=['id', 'product', 'wp', 'rp', 'sold'])

    df3 = pd.concat([df2, df], ignore_index=True)
    return df3

def update_col(col_name, id: list, values: list) -> DataFrame:
    df = add_items()
    print(f"initial df: \n {df}")
    df.loc[id, col_name] = values
    return df

def print_selected(rows: [], cols: [], df: DataFrame) -> DataFrame:
    return df.loc[rows, cols]

def add_product(row) -> DataFrame:
    df = add_items()
    df.loc[len(df)] = row
    return df

def add_column(name, data: list):
    new_product = [25, "bhagavatham", 999, 0, 10000000]
    df = add_product(new_product)
    print(df)
    df[name] = data
    return df

def get_descriptive_stats(df: DataFrame):
    return df.describe()

def greater_than_avg():
    df = build_data()
    return df.query('sold < sold.mean()')[['id', 'product']]

def lesser_units():
    df = build_data()
    return df.query('sold < 100')[['id', 'product']]


def best_quantile_products():
    df = build_data()
    return df.query('sold < sold.quantile(0.25)')[['id', 'product']]

if __name__ == '__main__':
    # print(add_items())
    # print(update_col('sold', [0, 1 ,2], [300,400,500]))
    # df = update_col('sold', [0, 1 ,2], [300,400,500])
    # print(print_selected([4,5,6], ['wp', 'rp'], df))
    # new_product = [25, "bhagavatham", 999, 0, 10000000]
    # print(add_product(new_product))
    # column_data = ["electronics", "food", "food", "food", "food", "food", "food", "food", "book"]
    # df = add_column('deparment', column_data)
    # print(get_descriptive_stats(df))
    print(best_quantile_products())
    print(lesser_units())
