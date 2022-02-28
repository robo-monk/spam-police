import pandas as pd

path = "./data/participants.csv"

df = pd.read_csv(path)


print(df.columns)
