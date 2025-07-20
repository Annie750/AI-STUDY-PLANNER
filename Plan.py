import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Generate synthetic training data
np.random.seed(42)
num_samples = 100

data = {
    "past_score": np.random.randint(40, 95, size=num_samples),
    "difficulty": np.random.randint(1, 6, size=num_samples),
    "trend": np.random.choice([-1, 0, 1], size=num_samples),
}

df = pd.DataFrame(data)

df["study_hours"] = (
    1 +
    (100 - df["past_score"]) * 0.05 +
    df["difficulty"] * 0.8 +
    (df["trend"] == -1) * 2 +
    (df["trend"] == 0) * 1 +
    (df["trend"] == 1) * 0.5
)

noise = np.random.normal(0, 0.3, size=num_samples)
df["study_hours"] = df["study_hours"] + noise
df["study_hours"] = df["study_hours"].clip(lower=1)

X = df[["past_score", "difficulty", "trend"]]
y = df["study_hours"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print(f"Model R² score: {score:.2f}")

joblib.dump(model, "study_time_predictor.pkl")
