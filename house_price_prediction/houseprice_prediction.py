import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("house_data.csv")


# Show columns
print(df.columns)


# Remove missing values
df = df.dropna()


# Features and target (based on your dataset)
X = df[['SquareFeet', 'Bedrooms', 'Bathrooms', 'YearBuilt']]
y = df['Price']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Predict
y_pred = model.predict(X_test)


# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))


# Plot
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()


# New house prediction
new_house = np.array([[2500, 3, 2, 2005]])

predicted_price = model.predict(new_house)

print("Predicted House Price:", predicted_price[0])
