import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define file paths
node_file_path = "/mnt/data/node.csv"
link_file_path = "/mnt/data/link.csv"

# Load datasets
node_df = pd.read_csv(node_file_path)
link_df = pd.read_csv(link_file_path)

# Display basic information
node_info = node_df.info()
link_info = link_df.info()

# Display summary statistics
node_summary = node_df.describe(include="all")
link_summary = link_df.describe(include="all")

# Check for missing values
node_missing = node_df.isnull().sum()
link_missing = link_df.isnull().sum()

# Visualize distributions of key numeric variables
plt.figure(figsize=(12, 5))
sns.histplot(node_df['latitude'], bins=30, kde=True, label="Latitude")
sns.histplot(node_df['longitude'], bins=30, kde=True, label="Longitude", color="orange")
plt.legend()
plt.title("Distribution of Node Coordinates")
plt.show()

plt.figure(figsize=(12, 5))
sns.histplot(link_df['free_flow_speed'].dropna(), bins=30, kde=True, label="Free Flow Speed")
sns.histplot(link_df['capacity'].dropna(), bins=30, kde=True, label="Capacity", color="orange")
plt.legend()
plt.title("Distribution of Link Attributes (Speed & Capacity)")
plt.show()

# Save results
eda_results = {
    "node_info": node_info,
    "link_info": link_info,
    "node_summary": node_summary,
    "link_summary": link_summary,
    "node_missing": node_missing,
    "link_missing": link_missing
}

# Display data summaries
import ace_tools as tools
tools.display_dataframe_to_user(name="Node Data Summary", dataframe=node_summary)
tools.display_dataframe_to_user(name="Link Data Summary", dataframe=link_summary)

# Update visualization to use correct coordinate columns
plt.figure(figsize=(12, 5))
sns.histplot(node_df['x_coord'], bins=30, kde=True, label="X Coordinate")
sns.histplot(node_df['y_coord'], bins=30, kde=True, label="Y Coordinate", color="orange")
plt.legend()
plt.title("Distribution of Node Coordinates (X, Y)")
plt.show()

plt.figure(figsize=(12, 5))
sns.histplot(link_df['free_speed'].dropna(), bins=30, kde=True, label="Free Flow Speed")
sns.histplot(link_df['capacity'].dropna(), bins=30, kde=True, label="Capacity", color="orange")
plt.legend()
plt.title("Distribution of Link Attributes (Speed & Capacity)")
plt.show()
