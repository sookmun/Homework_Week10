import pandas as pd

df = pd.read_csv('2020.csv')
region=df['Regional indicator'].unique()
gdp=df["Logged GDP per capita"].max()
gdp2=df["Logged GDP per capita"].min()
# print(region)
print(gdp,gdp2)
# gen=df["Generosity"].max()
# gen2=df["Generosity"].min()
# print(gen,gen2)