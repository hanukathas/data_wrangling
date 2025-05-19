import pandas as pd
import numpy as np
from numpy.ma.core import get_data
from pandas import Series


def generate_scores(min_score, max_score, counts):
    g = np.random.default_rng()
    scores = g.integers(low=min_score, high=max_score, size=counts)
    return Series(scores)


def set_data():
    s = generate_scores(70, 100, 10)
    s.index = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
    return s


def get_mean(months = 0, is_lead = True):
    s = set_data()
    if months == 0:
        mean = s.iloc[:].mean() #iloc gets the numerical means
    elif is_lead:
        mean = s.iloc[months:].mean()
    else:
        mean = s.iloc[:months].mean()
    print(f"mean is {mean}")

def get_head(count = 5):
    s = set_data()
    return s.head(n = 2)

def get_tail(count = 5):
    s = set_data()
    return s.tail(n = 3)

def get_mean_between(between: []):
    s = set_data()
    if len(between) == 0:
        mean = s.iloc[:].mean()
    else:
        mean = s.iloc[between[0]: between[1]].mean()
    print(f"mean between {between[0]} and {between[1]} is {mean}")

def get_best():
    s = set_data()
    print(s)
    print(s.idxmax(), s.max())

def series_print():
    s = set_data()
    return s.loc[:]

def get_perf():
    """
    performance between top and bottom five
    :return:
    """
    s = set_data()

    first_five = s.head().mean()
    last_five = s.tail().mean()

    print(f"difference is {round(abs(first_five - last_five), 2)}")

if __name__ == '__main__':
    # print(set_data())
    # get_mean()
    # get_mean(5)
    # get_mean(5, False)

    # print(get_head())
    # print(get_tail())
    # get_perf()
    # get_best()
    print(series_print())

