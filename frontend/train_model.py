from sklearn.linear_model import LinearRegression
import joblib
import numpy as np

# Training data with 5 features:
# [transport_mode, fuel_type, fuel_consumption (liters), distance_traveled (km), passengers]
X = np.array([
    [1, 0, 5, 100, 1],  # Car, Petrol, 5L, 100km, 1 passenger
    [0, 1, 3, 50, 2],   # Bike, Diesel, 3L, 50km, 2 passengers
    [1, 0, 10, 200, 3], # Car, Petrol, 10L, 200km, 3 passengers
    [0, 1, 7, 150, 1]   # Bike, Diesel, 7L, 150km, 1 passenger
])

y = np.array([20, 10, 35, 18])  # Corresponding carbon footprint

# Train model
model = LinearRegression()
model.fit(X, y)

# Save trained model
joblib.dump(model, "carbon_model.pkl")

print("✅ Model trained and saved as 'carbon_model.pkl'")
