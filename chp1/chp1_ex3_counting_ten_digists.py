import numpy as np
from pandas import Series


def generate_data():
    g = np.random.randint(0, 100, 10)
    s = Series(g)
    s.index = '1 2 3 4 5 6 7 8 9 10'.split()
    return s

def generate_boolean_series():
    s = generate_data()
    bool_s = s < 75
    return bool_s


if __name__ == '__main__':
    print(generate_boolean_series())