from sklearn.linear_model import LinearRegression
import pandas as pd

def train_model():
    df = pd.read_csv("../data/ecommerce_data.csv")
    df["day"] = range(len(df))

    X = df[["day"]]
    y = df["revenue"]

    model = LinearRegression()
    model.fit(X, y)

    return model
