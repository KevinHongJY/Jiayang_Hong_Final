# Import necessary libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Simulating dataset for RD analysis
np.random.seed(42)
n = 1000  # Number of observations

# Running variable: Vehicle emission standard score (continuous variable around the cutoff)
running_variable = np.random.normal(loc=5, scale=1, size=n)  # Emission scores centered around 5

# Policy cutoff: Vehicles above score of 5 are exempt from congestion fee
cutoff = 5
treatment = (running_variable >= cutoff).astype(int)  # 1 if exempt, 0 if not

# Outcome variable: Average travel speed (higher = less congestion)
true_effect = 2  # Hypothetical causal effect of policy
baseline_speed = 20 + norm.rvs(0, 2, n)  # Baseline travel speed
outcome = baseline_speed + true_effect * treatment + norm.rvs(0, 1, n)  # Apply treatment effect

# Create dataframe
df = pd.DataFrame({"Emission_Score": running_variable, "Treatment": treatment, "Travel_Speed": outcome})

# Plot travel speed against emission score to visualize discontinuity
plt.figure(figsize=(10,6))
sns.scatterplot(x=df["Emission_Score"], y=df["Travel_Speed"], hue=df["Treatment"], alpha=0.6)
plt.axvline(x=cutoff, color='red', linestyle='--', label="Policy Cutoff (Emission Score 5)")
plt.xlabel("Vehicle Emission Score")
plt.ylabel("Average Travel Speed (km/h)")
plt.title("Regression Discontinuity: Congestion Pricing Exemption Effect")
plt.legend()
plt.show()

# Estimation: Running RD regression
df["Intercept"] = 1  # Add intercept for OLS regression
model = sm.OLS(df["Travel_Speed"], df[["Intercept", "Treatment"]]).fit()

# Display regression results
rd_results = model.summary()
print(rd_results)

# Conducting robustness checks: Running RD with a narrower bandwidth around cutoff
bandwidth = 1  # Define the range around the cutoff
df_narrow = df[(df["Emission_Score"] >= cutoff - bandwidth) & (df["Emission_Score"] <= cutoff + bandwidth)]

# Running OLS on restricted dataset
model_narrow = sm.OLS(df_narrow["Travel_Speed"], df_narrow[["Intercept", "Treatment"]]).fit()

# Display robustness check results
rd_robustness_results = model_narrow.summary()
print(rd_robustness_results)

# Sensitivity Analysis: Checking if results hold across different bandwidths
bandwidths = [0.5, 1, 1.5, 2]  # Testing multiple bandwidths
sensitivity_results = []

for bw in bandwidths:
    df_bw = df[(df["Emission_Score"] >= cutoff - bw) & (df["Emission_Score"] <= cutoff + bw)]
    model_bw = sm.OLS(df_bw["Travel_Speed"], df_bw[["Intercept", "Treatment"]]).fit()
    sensitivity_results.append({"Bandwidth": bw, "Treatment Effect": model_bw.params["Treatment"], "P-Value": model_bw.pvalues["Treatment"]})

# Convert to DataFrame for visualization
sensitivity_df = pd.DataFrame(sensitivity_results)

sensitivity_df
