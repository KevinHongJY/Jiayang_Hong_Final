# **Machine Learning for Transportation Analysis**

## **Authors**
- **Jiayang Hong** – Lead Researcher, Model Development, and Analysis  
- **[Additional Team Members if applicable]** – Contributions in data processing, evaluation, and documentation  

## **Disclaimer**
This project was submitted as part of **STATS201: Machine Learning for Social Science**, instructed by **Prof. Luyao Zhang** at **Duke Kunshan University** in **Autumn 2025**. The findings, interpretations, and conclusions presented in this report are those of the authors and do not represent the views of Duke Kunshan University or its affiliates.

## **Acknowledgments**
We extend our gratitude to **Prof. Luyao Zhang** for valuable guidance throughout this research, as well as classmates for their feedback and discussions. We also acknowledge the contributions of **AI-assisted tools (e.g., ChatGPT, GitHub Copilot, Hugging Face models)** and **open-source libraries** such as `scikit-learn`, `XGBoost`, `matplotlib`, and `pandas`, which facilitated the execution of this project.

## **Statement of Intellectual and Professional Growth**
This project has deepened my understanding of **machine learning applications in social science**, particularly in **transportation modeling**. Through building predictive models for congestion forecasting, I have strengthened my skills in **data preprocessing, supervised learning, feature engineering, and model evaluation**. The experience also honed my ability to translate **machine learning insights into policy-relevant recommendations**, a crucial skill for data-driven decision-making in real-world applications.

---

## **Table of Contents**
- [Introduction](#introduction)
- [Research Objectives](#research-objectives)
- [Methodology](#methodology)
- [Results](#results)
- [Repository Navigation](#repository-navigation)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contact](#contact)

---

## **Introduction**
This study investigates the use of **supervised machine learning** to predict **congestion levels in urban transportation networks**. Using the **General Modeling Network Specification (GMNS)** dataset, the project develops and evaluates models that leverage **road capacity, free speed, number of lanes, and time of day** to forecast congestion levels. The findings provide actionable insights for **urban planners, policymakers, and transportation agencies**.

## **Research Objectives**
- Develop a **machine learning model for predicting congestion levels** based on real-world transportation data.
- Assess the effectiveness of **Random Forest and XGBoost** in forecasting congestion.
- Identify **key transportation features influencing congestion** to improve **urban mobility planning**.

## **Methodology**
- **Data Preprocessing**:  
  The dataset includes attributes such as **road capacity, free flow speed, number of lanes, and time of day**. Data preprocessing involved handling missing values, normalizing numerical features, and encoding categorical variables where applicable. The **congestion level** was derived from existing traffic data and adjusted to reflect realistic congestion patterns based on speed, capacity, and lane configurations.

- **Supervised Learning Models**:  
  The study applied **Random Forest Regressor** and **XGBoost**, two ensemble learning techniques known for their ability to capture nonlinear relationships. An **80-20 train-test split** was applied, and **five-fold cross-validation** was used to enhance model generalizability and reduce overfitting.

- **Hyperparameter Tuning**:  
  Grid Search optimization was applied to tune key parameters such as the number of estimators, tree depth, and learning rate.

- **Model Evaluation**:  
  Performance was assessed using **Root Mean Squared Error (RMSE), R² Score, and Mean Absolute Error (MAE)**.

- **Feature Importance Analysis**:  
  Identifying key predictors, including road capacity and free speed, to understand their impact on congestion patterns.

## **Results**
### **Model Performance Comparison**
| Model            | RMSE     | R² Score | MAE      |
|-----------------|----------|----------|----------|
| Random Forest   | 4.039    | 0.913    | 2.403    |
| XGBoost        | 4.065    | 0.912    | 2.426    |

The **Random Forest model outperformed XGBoost**, achieving **lower RMSE and higher predictive accuracy**. This suggests that tree-based ensemble learning methods effectively capture **complex congestion patterns** in transportation networks.

### **Feature Importance Analysis**
Feature importance analysis confirmed that **road capacity and free speed** are the most influential predictors of congestion. The number of lanes also plays a significant role, as fewer lanes contribute to higher congestion levels.

### **Prediction vs. Actual Congestion Levels**
To validate model performance, actual congestion levels were compared with predictions. The analysis demonstrated that the models effectively captured congestion trends, with **minimal residual errors**. Below is a visualization of actual vs. predicted congestion levels:

![Prediction vs. Actual Congestion](https://github.com/user-attachments/assets/sample_prediction_vs_actual.png)

---

## **Repository Navigation**
- **`/data`** – Contains raw and processed datasets.
- **`/code`** – Includes scripts for **data preprocessing, model training, evaluation, and visualization**.
- **`/notebooks`** – Jupyter notebooks detailing **step-by-step analysis**.
- **`/docs`** – Project documentation, references, and final report.

## **How to Use This Repository**
### **Setup Instructions**
1. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_REPO.git
   cd YOUR_GITHUB_REPO
