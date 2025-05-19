import numpy as np
from pandas import Series



def generate_series() -> Series:
    g = np.random.default_rng()
    s = g.integers(40, 60, 10)
    s = Series(s)
    s.index = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
    return s

def get_mean_series():
    s = generate_series()
    print(s)
    return s.mean()

def get_mean_diff():
    s = generate_series()
    print(s)
    mean_val = 80 - s.mean()
    print(mean_val)
    s = s + mean_val
    return s


if __name__ == '__main__':
    print(get_mean_diff())

