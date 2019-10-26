import pandas 

df = pandas.read_excel("sample.xlsx")
print(df[df['Age'] > 22])
print(df.head())
print(df.tail())
print(df.iloc[0:10])