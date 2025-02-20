# House Price Prediction

This project implements a house price prediction system using Linear Regression. It is built as an end-to-end machine-learning project using Flask.

## Overview

The goal of this project is to predict the price of houses based on various features such as location, total square feet area, number of bathrooms, and number of bedrooms.

## Features

- **Predicts house prices** based on user input.
- **Web-based interface** for easy interaction.
- **Multiple ML models tested** to select the best one.
- **Uses Ridge Regression** as the final model after evaluation.
- **End-to-end ML project** integrated with Flask.

## Project Structure

The project is structured as follows:

- `app.py`: Flask web application for serving predictions.
- `model/`: Directory containing trained model and preprocessing objects.
- `dataset/`: Directory containing the dataset used for training.
- `templates/`: HTML templates for the web interface.


---

## 🏆 Model Selection Process

Several machine learning models were trained and evaluated using **5-Fold Cross-Validation**. The **Ridge Regression model** achieved the best performance.

| **Model**                     | **Mean Cross-Validation R² Score** |
|--------------------------------|------------------------------------|
| **Linear Regression**          | **0.8035** |
| **Lasso Regression**           | 0.7924 |
| **Ridge Regression**           | **0.8035** |
| **Decision Tree Regressor**     | 0.6526 |
| **Random Forest Regressor**     | 0.7607 |
| **XGBoost Regressor**          | 0.7144 |
| **SVR (Support Vector Regressor)** | 0.1645 |

✅ **Best Model Before Tuning:** **Ridge Regression**  
✅ **Final Selected Model:** **Ridge Regression**  
✅ **Final Test R² Score:** **0.8177**  

📌 **Why Ridge Regression?**  
- Performs **better than tree-based models** for this dataset.  
- **Prevents overfitting** by applying regularization.  
- Achieved the **highest cross-validation score**.  

---

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kindo-tk/house_price_prediction.git
   ```
2. **Navigate to the project directory:**

    ```sh
    cd .\house_price_prediction\
    ```

3. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    ```

4. **Activate the virtual environment:**

   ```sh
   .venv\Scripts\activate
   ```

5. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

6. **Run the Flask application:**

    ```sh
    python app.py
    ```
## Usage

1. Access the web application by navigating to http://localhost:5000 in your web browser.
2. Enter the required details such as location, total square feet area, number of bathrooms, and number of bedrooms.
3. Click on the "Predict Price" button to get the predicted house price.


## Technologies Used

- Python
- Flask
- HTML/CSS
- Bootstrap
- scikit-learn


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 
For any inquiries or feedback, please contact:

- <a href="https://www.linkedin.com/in/tufan-kundu-577945221/">Tufan Kundu (LinkedIn)</a>
- Email: tufan.kundu11@gmail.com
<hr>
<br>
<img src="https://github.com/kindo-tk/images/blob/main/house1.png">
<img src = "https://github.com/kindo-tk/images/blob/main/Screenshot%202025-02-20%20235337.png">
