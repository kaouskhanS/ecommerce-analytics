import pandas as pd
import numpy as np

np.random.seed(42)

n = 50000

data = pd.DataFrame({
    "order_id": range(n),
    "customer_id": np.random.randint(1000, 5000, n),
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], n),
    "price": np.random.randint(100, 5000, n),
    "quantity": np.random.randint(1, 5, n),
    "order_date": pd.date_range(start="2023-01-01", periods=n, freq="H"),
    "returned": np.random.choice([0,1], n, p=[0.9,0.1])
})

data["revenue"] = data["price"] * data["quantity"]

data.to_csv("ecommerce_data.csv", index=False)
