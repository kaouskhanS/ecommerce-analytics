import pandas as pd

df = pd.read_csv("../data/ecommerce_data.csv")

df["order_date"] = pd.to_datetime(df["order_date"])
df["day_type"] = df["order_date"].dt.dayofweek.apply(lambda x: "Weekend" if x>=5 else "Weekday")

print(df.groupby("category")["revenue"].sum())
print(df.groupby("day_type")["revenue"].sum())
