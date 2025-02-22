# Implementing Supervised Machine Learning for Congestion Prediction using Random Forest and XGBoost

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Simulated dataset: GMNS-based node and link features for congestion prediction
np.random.seed(42)
n = 1000

# Creating synthetic traffic dataset with realistic attributes
traffic_data = pd.DataFrame({
    "Hour": np.random.randint(0, 24, n),  # Time of day
    "Lane_Capacity": np.random.randint(1, 5, n),  # Number of lanes
    "Intersection_Type": np.random.choice(["Signalized", "Unsignalized"], n),  # Traffic signals
    "Free_Flow_Speed": np.random.randint(30, 80, n),  # Speed limit
    "Congestion_Pricing": np.random.choice([0, 1], n),  # Whether congestion pricing applies
    "Adaptive_Signal": np.random.choice([0, 1], n),  # Whether adaptive signals are used
    "Congestion_Level": np.random.randint(0, 100, n)  # Target variable: Congestion level (0-100%)
})

# Convert categorical feature (Intersection_Type) into numeric
traffic_data["Intersection_Type"] = traffic_data["Intersection_Type"].map({"Signalized": 1, "Unsignalized": 0})

# Splitting dataset into train and test sets (80-20 split)
X = traffic_data.drop(columns=["Congestion_Level"])
y = traffic_data["Congestion_Level"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training Random Forest Regressor with cross-validation
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Training XGBoost Regressor
xgb = XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, random_state=42)
xgb.fit(X_train, y_train)

# Predictions
rf_pred = rf.predict(X_test)
xgb_pred = xgb.predict(X_test)

# Model Evaluation
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)

xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
xgb_r2 = r2_score(y_test, xgb_pred)
xgb_mae = mean_absolute_error(y_test, xgb_pred)

# Print evaluation metrics
print(f"Random Forest - RMSE: {rf_rmse:.2f}, R² Score: {rf_r2:.2f}, MAE: {rf_mae:.2f}")
print(f"XGBoost - RMSE: {xgb_rmse:.2f}, R² Score: {xgb_r2:.2f}, MAE: {xgb_mae:.2f}")

# Visualization: Actual vs. Predicted Congestion Levels
plt.figure(figsize=(10,5))
plt.scatter(y_test, rf_pred, label="Random Forest", alpha=0.5, color='blue')
plt.scatter(y_test, xgb_pred, label="XGBoost", alpha=0.5, color='red')
plt.plot([0, 100], [0, 100], "--", color='black', label="Perfect Prediction")
plt.xlabel("Actual Congestion Level (%)")
plt.ylabel("Predicted Congestion Level (%)")
plt.title("Congestion Prediction: Random Forest vs. XGBoost")
plt.legend()
plt.show()







# Refining the Model with Advanced Evaluation Metrics and Feature Importance Analysis

from sklearn.inspection import permutation_importance

# Recalculate RMSE without the 'squared' argument issue
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)
rf_mae = mean_absolute_error(y_test, rf_pred)

xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
xgb_r2 = r2_score(y_test, xgb_pred)
xgb_mae = mean_absolute_error(y_test, xgb_pred)

# Advanced Evaluation Metrics: Mean Absolute Percentage Error (MAPE)
rf_mape = np.mean(np.abs((y_test - rf_pred) / y_test)) * 100
xgb_mape = np.mean(np.abs((y_test - xgb_pred) / y_test)) * 100

# Display refined evaluation metrics
evaluation_results = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost"],
    "RMSE": [rf_rmse, xgb_rmse],
    "R² Score": [rf_r2, xgb_r2],
    "MAE": [rf_mae, xgb_mae],
    "MAPE (%)": [rf_mape, xgb_mape]
})

# Feature Importance Analysis
rf_importance = permutation_importance(rf, X_test, y_test, n_repeats=10, random_state=42)
xgb_importance = permutation_importance(xgb, X_test, y_test, n_repeats=10, random_state=42)

# Convert feature importance to DataFrame
rf_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': rf_importance.importances_mean})
xgb_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': xgb_importance.importances_mean})

# Sort by importance
rf_importance_df = rf_importance_df.sort_values(by="Importance", ascending=False)
xgb_importance_df = xgb_importance_df.sort_values(by="Importance", ascending=False)

# Plot Feature Importance for Random Forest
plt.figure(figsize=(8,5))
sns.barplot(x=rf_importance_df["Importance"], y=rf_importance_df["Feature"], palette="Blues_r")
plt.title("Feature Importance - Random Forest")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.show()

# Plot Feature Importance for XGBoost
plt.figure(figsize=(8,5))
sns.barplot(x=xgb_importance_df["Importance"], y=xgb_importance_df["Feature"], palette="Reds_r")
plt.title("Feature Importance - XGBoost")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.show()

# Display Evaluation Results
# Display the evaluation results without using ace_tools
print("Model Evaluation Results:")
print(evaluation_results)

