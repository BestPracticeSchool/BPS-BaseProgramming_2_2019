import pandas as pd


df = pd.read_csv('trades.csv', names = ['Company', 'Price','Amount', 'DateTime'])
sber_df = df[df['Company'] == 'SBER']
first_interval_sber = sber_df[(sber_df['DateTime'] >= '2019-01-30 07:00:00.00000') & (sber_df['DateTime'] < '2019-01-30 07:05:00.00000')]
print(first_interval_sber.head())





