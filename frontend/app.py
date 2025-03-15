from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Try loading the model
try:
    model = joblib.load("carbon_model.pkl")
except:
    model = None

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Carbon Footprint Prediction API!",
        "usage": {
            "/predict": "POST - Send JSON data for prediction"
        }
    })

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded. Train the model first."}), 500

    try:
        data = request.json
        transport_mode = data.get("transport_mode")
        fuel_type = data.get("fuel_type")
        fuel_consumption = data.get("fuel_consumption")
        distance_traveled = data.get("distance_traveled")
        passengers = data.get("passengers")

        # Validate input
        if None in [transport_mode, fuel_type, fuel_consumption, distance_traveled, passengers]:
            return jsonify({"error": "Missing required fields!"}), 400

        # Convert transport mode and fuel type to numeric values
        transport_mode_value = 1 if transport_mode.lower() == "car" else 0
        fuel_type_value = 1 if fuel_type.lower() == "diesel" else 0

        # Create input array for model
        input_data = np.array([[transport_mode_value, fuel_type_value, fuel_consumption, distance_traveled, passengers]])

        # Get prediction
        predicted_footprint = model.predict(input_data)[0]

        # Calculate actual carbon footprint manually (Example: 2.31 kg CO2 per liter of petrol)
        carbon_factor = 2.31 if fuel_type.lower() == "petrol" else 2.68  # Example values
        calculated_footprint = fuel_consumption * carbon_factor

        return jsonify({
            "message": "Carbon footprint calculated successfully!",
            "input_data": {
                "transport_mode": transport_mode,
                "fuel_type": fuel_type,
                "fuel_consumption": fuel_consumption,
                "distance_traveled": distance_traveled,
                "passengers": passengers
            },
            "calculated_carbon_footprint (kg CO2)": round(calculated_footprint, 2),
            "model_predicted_carbon_footprint (kg CO2)": round(predicted_footprint, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
