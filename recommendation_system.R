library(recommenderlab)
library(dplyr)

# Load data
data <- read.csv("/Users/kannupriya/Downloads/archive (17)/sales_data.csv")

# Create a matrix for recommendations
ratings <- as(data, "realRatingMatrix")

# Train recommendation model using Collaborative Filtering
model <- Recommender(ratings, method = "UBCF")

# Generate recommendations for top 5 products for a user
recommendations <- predict(model, ratings[1, ], n = 5)
as(recommendations, "list")
