import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option("display.max_columns", 13)

df_deaths = pd.read_csv("deaths.csv")
df_deaths.drop(columns=["Lat", "Long"], inplace = True)

df_deaths["Total Deaths"] = df_deaths.sum(axis = 1)
df_deaths.drop(df_deaths.iloc[:, 2:73], axis = 1, inplace = True)

df_deaths.sort_values(['Total Deaths'], inplace = True, ascending = False)


df_confirmed = pd.read_csv("confirmed.csv")
df_confirmed.drop(columns=["Lat", "Long"], inplace = True)
df_confirmed["Total Confirmed Cases"] = df_confirmed.sum(axis = 1)
df_confirmed.drop(df_confirmed.iloc[:, 2:73], axis = 1, inplace = True)


df_confirmed = df_confirmed[df_confirmed['Country/Region'] == "Canada"]
df_confirmed.drop(df_confirmed.iloc[:, 0:2], axis = 1, inplace = True)

df_deaths = df_deaths[df_deaths['Country/Region'] == "Canada"]
print(df_deaths)

df = pd.concat([df_deaths, df_confirmed], axis = 1)
df['Death Rate %'] = (df['Total Deaths'] / df["Total Confirmed Cases"]) * 100
df.sort_values(["Death Rate %"], inplace = True, ascending = False)
print(df)