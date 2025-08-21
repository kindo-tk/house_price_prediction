# House Price Prediction

This project implements a house price prediction system using machine learning models. It is an end-to-end machine learning project integrated with Flask for web deployment.

---

## Overview

The goal of this project is to predict the price of houses in Bangalore based on various features such as:

- **Location**
- **Total square feet area**
- **Number of bathrooms**
- **Number of bedrooms (BHK)**

The project provides a **web-based interface** for users to input house details and get price predictions instantly.

---

## Features

- Predicts house prices based on user input.
- Web-based interface for easy interaction.
- Multiple machine learning models tested to select the best one.
- Uses **Ridge Regression** as the final model after evaluation.
- End-to-end ML project integrated with Flask.

---

## Project Structure

```
house_price_prediction/
│
├── app.py                  # Flask application
├── dataset/                # Dataset used for training
├── model/                  # Saved model and preprocessing objects
├── templates/              # HTML templates for the web interface
└── README.md               # Project documentation
```

---

##  Model Selection & Results

Several machine learning models were trained and evaluated using **5-Fold Cross-Validation**.  

| **Model**                     | **Mean Cross-Validation R² Score** |
|--------------------------------|------------------------------------|
| Linear Regression              | 0.8413 |
| Lasso Regression               | 0.8333 |
| Ridge Regression               | 0.8413 |
| Decision Tree Regressor        | 0.7397 |
| Random Forest Regressor        | 0.7869 |
| XGBoost Regressor              | 0.8328 |

- **Best Model Before Tuning:** Ridge Regression  
- **Final Selected Model:** Ridge Regression  

**Performance on Test Set:**  

- **R² Score:** 0.8016  
- **Mean Absolute Error (MAE):** 19.6350  
- **Root Mean Squared Error (RMSE):** 39.9124  

**Why Ridge Regression?**  

- Performs comparably to Linear Regression while adding **regularization** to prevent overfitting.  
- Achieved the **highest cross-validation score** alongside Linear Regression.  
- Provides **stable and reliable predictions** on the test set.

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/kindo-tk/house_price_prediction.git
```

2. Navigate to the project directory:

```bash
cd house_price_prediction
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

```bash
.venv\Scripts\activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Run the Flask application:

```bash
python app.py
```

7. Open your browser and go to:

```
http://localhost:5000
```

---

## Usage

1. Enter the required house details:

   - Location
   - Total square feet area
   - Number of bathrooms
   - Number of bedrooms (BHK)

2. Click **Predict Price** to see the estimated house price.

---

## Technologies Used

- Python
- Flask
- HTML/CSS
- Bootstrap
- scikit-learn
- XGBoost
- Babel (for Indian currency formatting)

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

For any inquiries or feedback, please contact:

- [Tufan Kundu (LinkedIn)](https://www.linkedin.com/in/tufan-kundu-577945221/)  
- Email: tufan.kundu11@gmail.com  

---

### Screenshots

<img src="https://github.com/kindo-tk/images/blob/main/house1.png" width="600">
<img src="https://github.com/kindo-tk/images/blob/main/Screenshot%202025-02-20%20235337.png" width="600">

