import pandas as pd

# This loads the Coke/Pepsi data you already have in your repo
df = pd.read_csv("pair_data.csv")

# Look at just the first 5 rows
print("--- THE DATA HEAD ---")
print(df.head())

# Filter: Find days where Pepsi (PEP) was cheaper than $140
cheap_pepsi = df[df['PEP'] < 140]

print("\n--- CHEAP PEPSI DAYS ---")
print(cheap_pepsi)