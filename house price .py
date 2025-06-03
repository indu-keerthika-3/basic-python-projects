import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data
data = {
    'Area': [1000, 1500, 1800, 2400, 3000],
    'Bedrooms': [2, 3, 4, 4, 5],
    'Age': [10, 5, 3, 2, 1],
    'Price': [200000, 300000, 400000, 500000, 600000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Area', 'Bedrooms', 'Age']]
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Output results
print("Predicted prices:", predictions)
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)