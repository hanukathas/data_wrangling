import numpy as np
from pandas import Series


def generate_data():
    g = np.random.default_rng(0)
    s = Series(g.normal(20, 5, 28))
    s.index = 'Sun Mon Tue Wed Thu Fri Sat'.split() * 4
    return s

if __name__ == '__main__':
    s = generate_data()
    s_mon =  s.loc['Mon']
    # print(s_mon)
    # print(s_mon.mean())
    # s_weekend = s.loc[['Sat', 'Sun']]
    # print(s_weekend.mean())
    s_diff_greater_2 = s.diff()
    s_diff_greater_2 = s[s_diff_greater_2 == -2]

