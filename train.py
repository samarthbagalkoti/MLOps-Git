import os, pickle, pandas as pd
from sklearn.linear_model import LinearRegression

DATA = os.getenv("DATA_PATH", "/data/data.csv")
OUT = os.getenv("MODEL_PATH", "/data/model.pkl")

df = pd.read_csv(DATA)
# Normalize headers
df.columns = [c.strip().lower() for c in df.columns]
col = "score" if "score" in df.columns else df.columns[0]

X = df[[col]]
y = df[col] * 2  # dummy target
model = LinearRegression().fit(X, y)
pickle.dump(model, open(OUT, "wb"))
print(f"✅ Trained and saved model to {OUT}")

