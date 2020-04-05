import pandas as pd

pd.set_option('display.width', 400)
pd.set_option("display.max_columns", 13)

df = pd.read_csv("Pokemon.csv")
print(df)

df['Power Level'] = df['Attack'] + df['Sp. Atk']
cols = list(df.columns)

df = df[cols[0:4] + [cols[13]] + cols[4:13]]
print(df.sort_values(['Power Level'], ascending = False))


df.drop(df.iloc[:,5:15], axis = 1, inplace = True)
print(df)

df.to_csv("newPokemon.csv")

