import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Load Data
df = pd.read_csv('diabetes.csv')

# 2. Split X, y
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# 3. Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train model
model = LogisticRegression()
model.fit(X_scaled, y)

# 5. Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved!")