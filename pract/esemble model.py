import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
# importing machine learning models for prediction
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.linear_model import LinearRegression
# loading train data set in dataframe from train_data.csv file
df = pd.read_csv("train_data.csv")
# getting target data from the dataframe
target = df["target"]
# getting train data from the dataframe
train = df.drop("target")
# Splitting between train data into training and validation dataset
X_train, X_test, y_train, y_test = train_test_split(
train, target, test_size=0.20)
# initializing all the model objects with default parameters
model_1 = LinearRegression()
37 | Pagemodel_2 = xgb.XGBRegressor()
model_3 = RandomForestRegressor()
# training all the model on the training dataset
model_1.fit(X_train, y_target)
model_2.fit(X_train, y_target)
model_3.fit(X_train, y_target)
# predicting the output on the validation dataset
pred_1 = model_1.predict(X_test)
pred_2 = model_2.predict(X_test)
pred_3 = model_3.predict(X_test)
# final prediction after averaging on the prediction of all 3 models
pred_final = (pred_1+pred_2+pred_3)/3.0
# printing the root mean squared error between real value and predictedvalue
print(mean_squared_error(y_test, pred_final))