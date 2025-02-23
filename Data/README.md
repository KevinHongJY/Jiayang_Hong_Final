# Data Folder Overview

This folder holds datasets from **Nature Research’s Scientific Data**. The primary files are hosted on Zenodo. You can access them here:[**Zenodo Record #4541153**](https://zenodo.org/records/4541153)
), which follows the General Modeling Network Specification (GMNS) format for node-link representations (`node.csv`, `link.csv`), supplemented by origin-destination (OD) matrices that capture time-dependent travel flows. By combining static structural attributes (nodes and links) with dynamic traffic flow data (OD matrices), researchers can analyze network congestion, test adaptive signal controls, and assess equity impacts. This multi-source approach enriches the overall model, providing a more nuanced view of urban transportation patterns and enabling scenario analyses across different times of day and various demand conditions.

---

## Data Dictionary

| **Variable**       | **Data Type**         | **Description**                                                                | **Possible Values / Examples**       |
|--------------------|-----------------------|--------------------------------------------------------------------------------|--------------------------------------|
| `node_id`          | Integer / String      | Unique identifier for each node                                               | e.g., `10001`, `10002`               |
| `latitude`         | Float                 | Node’s latitude coordinate (UTM or WGS84)                                      | `42.35`, `51.50`, etc.               |
| `longitude`        | Float                 | Node’s longitude coordinate (UTM or WGS84)                                     | `-71.06`, `-0.12`, etc.              |
| `node_type`        | Categorical           | Classification of the node (e.g., `external`, `centroid`, `signal`)           | `external`, `centroid`, `signal`     |
| `link_id`          | Integer / String      | Unique identifier for each link (road segment)                                | e.g., `20001`, `20002`               |
| `from_node_id`     | Integer / String      | ID of the node where the link starts                                          | Matches a valid `node_id`            |
| `to_node_id`       | Integer / String      | ID of the node where the link ends                                            | Matches a valid `node_id`            |
| `capacity`         | Integer               | Max allowable flow on the link (vehicles/hour)                                 | `1000`, `1200`, `2000`               |
| `free_flow_speed`  | Float                 | Typical link speed under uncongested conditions (km/h)                         | `50`, `60`, `90`                     |
| `number_of_lanes`  | Integer               | Total number of lanes on the link                                             | `1`, `2`, `3`                        |
| `od_matrix`        | 2D Array / CSV        | Origin-destination table representing trip counts or flows                    | e.g., `10x10`, `20x20` matrix        |
| `time_period`      | String / Categorical  | Indicates time grouping for OD data (e.g., `peak`, `off_peak`)                | `peak_morning`, `peak_evening`       |
| `bike_facility`    | Boolean / String      | Indicates presence of a bike lane or shared lane marking on the link          | `Yes`, `No`, `Shared Lane`           |

## **3. Preprocessing and Harmonization Steps**
1. **Missing Data Handling**  
   - Imputed missing values for emission scores and speed data using mean values.
   - Removed extreme outliers beyond **3 standard deviations**.

2. **Feature Engineering**
   - Converted categorical variables (e.g., intersection types) into **numerical encoding**.
   - Created **binary treatment indicator** for **congestion pricing policy**.

3. **Standardization and Scaling**
   - Normalized continuous features (e.g., speed, emissions) to ensure **model consistency**.
   - Applied **log transformation** on highly skewed variables.

4. **Train-Test Splitting**
   - The dataset for machine learning was split into **80% training** and **20% testing** sets.

**Note**: All coordinate data in `node.csv` use **UTM** unless stated otherwise, and OD matrices are typically aggregated in 15-minute intervals. For further details on data usage, see the main [`README.md`](../README.md) in the root directory.
