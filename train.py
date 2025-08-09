import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("/data/data.csv")
X = df[['score']]
y = df['score'] * 2  # dummy target
model = LinearRegression().fit(X, y)
pickle.dump(model, open("/data/model.pkl", "wb"))

