# **Code Folder: Machine Learning & Causal Inference in Transportation Analysis**

## **1. Overview**
This folder contains Python scripts and Jupyter Notebooks for **Natural Language Processing (NLP) analysis**, **congestion prediction using machine learning**, and **causal inference with Regression Discontinuity (RD) design**.

The main objectives of this codebase are:
- Extract insights from **policy-related textual data** using NLP techniques.
- Predict **congestion levels** using **Random Forest and XGBoost models**.
- Evaluate the **causal effect of congestion pricing policies** using RD analysis.

---

## **2. Files Included**
| File | Description |
|------|------------|
| `Explanation.py` | Performs **sentiment analysis** and **topic modeling** on transportation policy texts. |
| `prediction.py` | Applies **Random Forest & XGBoost** for congestion level prediction. |
| `causal_inference.ipynb` | Implements **Regression Discontinuity (RD) Analysis** to estimate the impact of congestion pricing policies. |

---

## **3. Explanation & Visualizations**
### **Natural Language Processing (NLP) Analysis**
This section provides an analysis of **sentiment trends and topic modeling** applied to transportation policy texts.

![Sentiment Score Distribution](https://github.com/user-attachments/assets/6f93f404-c408-480e-8bcf-73952429533f)
![Topic Importance](https://github.com/user-attachments/assets/6485018b-b460-4dee-9b7c-a90e884a57a0)

- **Sentiment Score Distribution:**  
  - Documents are analyzed using **VADER Sentiment Analyzer**.
  - **Negative scores** indicate complaints (e.g., toll increases).
  - **Positive scores** reflect supportive feedback (e.g., bike lane expansion).

- **Topic Modeling (LDA):**  
  - Identifies key themes in **transportation policy discussions**.
  - **Topic 1:** Congestion reduction & toll pricing.  
  - **Topic 2:** Public transit expansion & accessibility.

---

### **Congestion Prediction: Model Evaluation & Feature Importance**
Predictive modeling using **Random Forest** and **XGBoost** to forecast congestion trends.

![Congestion Prediction](https://github.com/user-attachments/assets/65334a84-aaed-4e8b-b4d4-709275868c24)
![Feature Importance - Random Forest](https://github.com/user-attachments/assets/3dc60b87-2b60-4a2a-bdac-5e53ddaefd0c)
![Feature Importance - XGBoost](https://github.com/user-attachments/assets/dcba2c2a-194b-4d07-89ed-8d4a0df58ae7)

- **Model Performance:**
  - **Random Forest outperforms XGBoost** but both require tuning.
  - **Congestion Pricing & Adaptive Signals** are key factors.
  - Feature importance varies between models.

---

### **Causal Inference: Regression Discontinuity (RD)**
Regression Discontinuity (RD) is used to analyze the impact of **congestion pricing policies** on vehicle speeds.

![RD Analysis](https://github.com/user-attachments/assets/56624bbc-0364-42c0-b8ff-eebbec1bc03f)
<img width="665" alt="Screenshot 2025-02-23 at 4 22 17 PM" src="https://github.com/user-attachments/assets/81cf2118-62ff-47a7-b443-df6745cf77be" />
<img width="361" alt="Screenshot 2025-02-23 at 4 22 33 PM" src="https://github.com/user-attachments/assets/4e6bb152-86fc-4754-89df-af30f15a62f0" />

- **Findings:**  
  - Vehicles **exempt from congestion pricing** (above cutoff) show a **2 km/h speed increase**.
  - Robustness checks confirm the **validity of RD assumptions**.
  - Sensitivity analysis across multiple bandwidths ensures **consistent effects**.

---

## **4. Prerequisites**
### **Required Libraries & Versions**
Ensure you have **Python 3.9+** installed. The required dependencies include:

```bash
pip install -r requirements.txt
