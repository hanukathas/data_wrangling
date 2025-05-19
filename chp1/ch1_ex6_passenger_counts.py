import pandas as pd
from pandas import DataFrame


def passenger_counts() -> DataFrame:
    s = pd.read_csv('/data/sample.csv').squeeze()
    return s

def get_pulses():
    s = passenger_counts()
    return s[['Pulse', 'Maxpulse']].value_counts(normalize=True)

def get_summary():
    s = passenger_counts()
    return pd.cut(s['Pulse'],
           bins=[s['Pulse'].quantile(.25), s['Pulse'].quantile(.50), s['Pulse'].quantile(.75), s['Pulse'].max()],
           labels=['25%', '50%', '75%']).value_counts()



if __name__ == '__main__':
    print(get_summary())