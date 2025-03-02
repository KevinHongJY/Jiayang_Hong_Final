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
# Machine Learning for Transportation Analysis

## Table of Contents
- [Code](./code)
  - [Explanation Notebook](./code/Explanation.ipynb)
  - [Causal Inference Notebook](./code/causal_inference.ipynb)
  - [Prediction Notebook](./code/prediction.ipynb)
- [Data](./data)
- [Visualizations](./visualizations)
- [Docs](./docs)
  - [Final Report](./docs/Final-Report.pdf)

## Code
The `code` directory contains all Python scripts and Jupyter notebooks used for this project. It includes methods for explanation (such as social network analysis), prediction (machine learning models), and causal inference (regression discontinuity design).

## Explanation Notebook
The [Explanation Notebook](./code/Explanation.ipynb) provides the script for social network analysis and related methods used to extract insights from the data.

## Causal Inference Notebook
The [Causal Inference Notebook](./code/causal_inference.ipynb) details the implementation of Regression Discontinuity Design (RDD) analysis to assess policy impacts.

## Prediction Notebook
The [Prediction Notebook](./code/prediction.ipynb) contains scripts for training and evaluating predictive models used in this study.

## Data
The `data` directory stores all raw and processed datasets used for analysis.

## Visualizations
The `visualizations` directory includes all plots and charts that illustrate the results of the analyses.

## Docs
The `docs` directory contains supplementary documentation and the final report.

## Final Report
The [Final Report](./docs/Final-Report.pdf) provides a comprehensive overview of the study, including the background, methodologies, results, and conclusions.

---

## **Repository Structure**
This repository is organized into clearly labeled directories:

### **Code**
Contains all Python scripts and Jupyter notebooks used in the project.
- `code/data_preprocessing.py` – Data cleaning and feature engineering.
- `code/model_training.py` – Training and evaluation of Random Forest and XGBoost models.
- `code/feature_importance.py` – Analysis of the most significant predictors.
- `notebooks/ML_Transportation_Analysis.ipynb` – Step-by-step workflow.

### **Data**
Contains raw and processed datasets used for analysis.
- `data/raw/` – Original GMNS dataset.
- `data/processed/` – Cleaned and preprocessed data files.

### **Visualizations**
Includes figures, charts, and tables that illustrate key findings.
- `visualizations/predictions_vs_actual.png`
- `visualizations/feature_importance.png`

### **Documentation**
Stores supplementary materials, reports, and references.
- `docs/final_report.pdf`
- `docs/references.bib`

---

## **How to Use This Repository**
### **Setup Instructions**
1. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_REPO.git
   cd YOUR_GITHUB_REPO
