import pandas as pd


df = pd.read_csv("./games_fixed_columns.csv")
df["Total Reviews"] = df["Positive"].fillna(0).astype(int) + df["Negative"].fillna(0).astype(int)

filtered_data = df[df["Total Reviews"] >= 50]

filtered_data["Positive Twice Negative"] = (
    filtered_data["Positive"].fillna(0).astype(int) >= 4 * filtered_data["Negative"].fillna(0).astype(int)
).astype(int)

positive_data = filtered_data.loc[filtered_data["Positive Twice Negative"] == 1]
negative_data = filtered_data.loc[filtered_data["Positive Twice Negative"] == 0]

positive_train = positive_data.sample(n=10000)
positive_test = positive_data.drop(positive_train.index).sample(n=500)

negative_train = negative_data.sample(n=10000)
negative_test = negative_data.drop(negative_train.index).sample(n=500)

train_data = pd.concat([positive_train, negative_train]).sample(frac=1)
test_data = pd.concat([positive_test, negative_test]).sample(frac=1)

train_data.to_csv("games_train.csv", index=False)
test_data.to_csv("games_test.csv", index=False)
