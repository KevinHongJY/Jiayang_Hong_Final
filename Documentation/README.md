1. Overview
Goal: Investigate congestion patterns, route choices, and time-dependent attributes in a GMNS-formatted dataset.
Key Tools:
Python 3.8+ (or R 4.x, if using R scripts)
Libraries: pandas, numpy, geopandas, and matplotlib for visualization
Optional AI Tools: Hugging Face Transformers (for data augmentation), GitHub Copilot (for code assistance)
Main Scripts:
data_cleaning.py: Cleans and merges the GMNS CSV files (node.csv, link.csv)
traffic_assignment.py: Runs the core static/dynamic assignment methods
2. Local Setup
Install Python
## Dependencies

Below is a summary of the key dependencies:

| Library       | Version  | Purpose                                          |
|---------------|----------|--------------------------------------------------|
| numpy         | 1.22.0   | Numerical computations                           |
| pandas        | 1.4.0    | Data manipulation and analysis                   |
| geopandas     | 0.10.2   | Geospatial data processing                       |
| matplotlib    | 3.5.0    | Plotting and visualization                       |
| seaborn       | 0.12.2   | Statistical data visualization                   |
| scikit-learn  | 1.2.2    | Machine learning models and utilities            |
| xgboost       | 1.7.5    | Gradient boosting for predictive modeling        |
| shap          | 0.41.0   | Model interpretability and feature importance      |
| statsmodels   | 0.14.0   | Statistical modeling and regression analysis       |
| jupyter       | Latest   | Running Jupyter notebooks                        |

Ensure you have Python 3.8 or higher installed before proceeding.

```bash
pip install -r requirements.txt

Recommended: Anaconda Python 3.8+ for easy package management.
2. Create a Virtual Environment:
```python
python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate
pip install -r requirements.txt
```
3. Install Required Packages
```bash
pip install -r requirements.txt
```
where requirements.txt might include:
```python
pandas==1.4.0
numpy==1.22.0
geopandas==0.10.2
matplotlib==3.5.0
# Optional AI Tools
transformers==4.26.0
```
4. Configure Data Paths
Place all GMNS CSV files (node.csv, link.csv, etc.) inside data/.
Update any file paths within data_cleaning.py or other scripts if you’ve moved or renamed directories.
5. Run the Analysis
```bash
python code/data_cleaning.py
python code/traffic_assignment.py
```
3. Cloud Setup
Option A: Google Colab

Upload Repository
Zip and upload the entire repository to your Google Drive or clone it from GitHub within a Colab notebook.
Create a Colab Notebook
Install dependencies:
```python
!pip install geopandas matplotlib transformers
```
3. Execute Scripts
Run each Python script with:
```python
!python code/causal_inference.py
!python code/explaination.py
!python code/prediction.py
```
For a more interactive approach, open the problemset_2.ipynb notebook:
```python
jupyter notebook problemset_2.ipynb
```

4. Clone Repo and Run
```python
[git clone https://github.com/KevinHongJY/Jiayang_Hong_Final.git
]
cd my-gmns-project
]

```
