import pandas as pd

df = pd.read_csv("./games_fixed_columns.csv")

subset = df.head(200)
subset.to_csv("test.csv", index=False)

remaining_records = df.iloc[200:]
remaining_records.to_csv("train.csv", index=False)