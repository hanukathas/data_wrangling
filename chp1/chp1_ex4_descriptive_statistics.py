import numpy as np
from pandas import Series


def generate_data() -> Series:
    g = np.random.default_rng(0)
    s = Series(g.normal(0, 100, 100_000))
    return s

def describe_data():
    s = generate_data()

    return s.describe()

def get_for_5_times_max():
    s = generate_data()
    s.iloc[s == s.min()] = 5 * s.max()
    return s.describe()


if __name__ == '__main__':
    print(describe_data())
    print(get_for_5_times_max())


