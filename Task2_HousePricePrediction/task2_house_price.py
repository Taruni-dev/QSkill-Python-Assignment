#Donloaded the House Price Prediction dataset from Kaggle
#pip install pandas numpy scikit-learn matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("dataset.csv")

# Select features and target
X = df.select_dtypes(include='number').drop(columns=[df.select_dtypes(include='number').columns[-1]])
y = df.select_dtypes(include='number').iloc[:, -1]

# Handle missing values
X.fillna(X.mean(), inplace=True)
y.fillna(y.mean(), inplace=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, y_pred)
print("Model Accuracy (R2 Score):", accuracy)

# Plot Actual vs Predicted
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
