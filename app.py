import numpy as np
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Simulated SCM data (replace with real data in a production scenario)
dates = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)  # Days
demand = np.array([100, 120, 115, 130, 140, 135, 150])  # Units demanded
inventory = [200, 180, 165, 150, 130, 110, 90]  # Stock levels
shipping_delays = [1, 2, 1, 3, 2, 4, 3]  # Delay days

# Train a simple demand prediction model
model = LinearRegression()
model.fit(dates, demand)

# Predict demand for next 3 days
future_dates = np.array([8, 9, 10]).reshape(-1, 1)
predicted_demand = model.predict(future_dates).tolist()

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/data')
def get_data():
    data = {
        'dates': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'demand': demand.tolist() + predicted_demand,
        'inventory': inventory + [80, 70, 60],  # Simulated future inventory
        'shipping_delays': shipping_delays + [2, 1, 2]  # Simulated future delays
    }
    return jsonify(data)

def main():
    print(">>> Starting Flask server...")
    app.run(debug=True)

if __name__ == "__main__":
    main()