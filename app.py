from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
from babel.numbers import format_currency
import os
from pathlib import Path

app = Flask(__name__)

# Define file paths
DATA_PATH = Path("dataset/cleaned_house_data.csv")
MODEL_PATH = Path("model/BestModel.pkl")

# Load data and model with error handling
try:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset file not found at {DATA_PATH}")
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    data = pd.read_csv(DATA_PATH)
    pipe = pickle.load(open(MODEL_PATH, 'rb'))
    locations = sorted(data['location'].unique())
except Exception as e:
    raise Exception(f"Error loading data or model: {str(e)}")

@app.route('/')
def index():
    try:
        return render_template('index.html', locations=locations)
    except Exception as e:
        return f"Error: An error occurred: {str(e)}", 200  
    
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        location = request.form.get('location')
        bhk = request.form.get('bhk')
        bath = request.form.get('bath')
        sqft = request.form.get('total_sqft')

        # Validate inputs
        if not all([location, bhk, bath, sqft]):
            return "Error: All fields are required", 200  
        
        if location not in locations:
            return "Error: Invalid location selected", 200  

        try:
            bhk = int(bhk)
            bath = float(bath)
            sqft = float(sqft)
        except ValueError:
            return "Error: BHK, bathrooms, and square footage must be numeric", 200  

        # Create input DataFrame
        input_data = pd.DataFrame([[location, sqft, bath, bhk]], 
                                 columns=['location', 'total_sqft', 'bath', 'BHK'])

        # Make prediction
        prediction = pipe.predict(input_data)[0] * 1e5

        # Format as Indian currency
        formatted_prediction = format_currency(prediction, "INR", locale="en_IN")

        return formatted_prediction

    except Exception as e:
        return f"Error: An error occurred: {str(e)}", 200  

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host=host, port=port, debug=debug)