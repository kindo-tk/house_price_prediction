from flask import Flask, render_template, request
import pandas as pd 
import pickle
import numpy as np
from babel.numbers import format_currency  # Import Babel for Indian currency formatting

app = Flask(__name__)
data = pd.read_csv("dataset/cleaned_house_data.csv")
pipe = pickle.load(open("model/BestModel.pkl", 'rb'))

@app.route('/')
def index():
    try:
        locations = sorted(data['location'].unique())
        return render_template('index.html', locations=locations)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form.get('location')
        bhk = int(request.form.get('bhk'))
        bath = float(request.form.get('bath'))
        sqft = float(request.form.get('total_sqft'))
        
        # Create a DataFrame with the input data
        input_data = pd.DataFrame([[location, sqft, bath, bhk]], columns=['location', 'total_sqft', 'bath', 'BHK'])
        
        # Make prediction
        prediction = pipe.predict(input_data)[0] * 1e5

        # Format as Indian currency (₹)
        formatted_prediction = format_currency(prediction, "INR", locale="en_IN")

        return formatted_prediction

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
