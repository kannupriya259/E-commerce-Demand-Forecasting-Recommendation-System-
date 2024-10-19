# E-commerce-Demand-Forecasting-Recommendation-System-
Predicting future demand ensures that businesses maintain the right inventory levels, reducing stockouts and overstock situations. This module uses Facebook Prophet, a robust time-series forecasting tool, to analyze historical sales data and generate sales predictions for the upcoming periods.
1. Demand Forecasting
Predicting future demand ensures that businesses maintain the right inventory levels, reducing stockouts and overstock situations. This module uses Facebook Prophet, a robust time-series forecasting tool, to analyze historical sales data and generate sales predictions for the upcoming periods.

Key Features:

Time-series analysis using Prophet library.
Forecast future sales trends for the next 30 days.
Output includes confidence intervals (yhat_lower, yhat_upper) to help stakeholders make informed decisions.
Results are saved as forecast_results.csv for further reporting.
Technologies:

Python: Data preprocessing and model training.
Prophet: Time-series forecasting model for demand predictions.
2. Recommendation System
The recommendation system aims to increase customer engagement by suggesting relevant products based on user behavior. The project employs User-Based Collaborative Filtering (UBCF) using R's recommenderlab package to generate personalized recommendations.

Key Features:

Collaborative filtering to recommend products.
Handles sparse data through matrix factorization techniques.
Generates a list of top n recommended products for each user.
Useful for personalized email marketing and on-site product suggestions.
Technologies:

R: Implementation of collaborative filtering.
recommenderlab: Library for recommendation algorithms.
Data Flow
Data Collection: Upload sales data in CSV format to the data/ folder.
Preprocessing: Python scripts in the scripts/ folder clean and transform the data for analysis.
Demand Forecasting: Use the Prophet model to predict future demand and store the results in forecast_results.csv.
Recommendation System: Use R to train a recommendation model on customer purchase behavior, generating top product suggestions.
