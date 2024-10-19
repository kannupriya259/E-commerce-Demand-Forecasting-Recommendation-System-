# E-commerce Demand Forecasting & Recommendation System

This project demonstrates demand forecasting and product recommendations using Python, R, and machine learning. It focuses on improving stock management and personalized recommendations for e-commerce businesses.

## Features
- **Demand Forecasting:** Predicts future demand using historical sales data.
- **Recommendation System:** Recommends products based on customer behavior and item similarity.
- **Tech Stack:** Python, R, Machine Learning (Prophet, XGBoost, Collaborative Filtering).

## Setup
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/ecommerce-demand-forecasting-recommendation.git
   cd ecommerce-demand-forecasting-recommendation
pip install -r requirements.txt
install.packages(c("recommenderlab", "dplyr"))

---

## Step 2: `requirements.txt`

```plaintext
pandas
scikit-learn
xgboost
prophet
matplotlib
import pandas as pd

def load_and_preprocess_data('/Users/kannupriya/Downloads/archive (17)'):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values('Date')
    print("Data Loaded Successfully")
    return data

if __name__ == "__main__":
    data = load_and_preprocess_data('/Users/kannupriya/Downloads/archive/data/sales_data.csv')
from prophet import Prophet
import pandas as pd

def forecast_sales(data):
    model = Prophet()
    data = data.rename(columns={'Date': 'ds', 'Sales': 'y'})
    model.fit(data)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

if __name__ == "__main__":
    data = pd.read_csv('data/sales_data.csv')
    forecast = forecast_sales(data)
    forecast.to_csv('results/forecast_results.csv', index=False)
    print("Forecasting Completed and Saved")

