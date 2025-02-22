# Jiayang_Hong_PS2
Project: GMNS Data Analysis
Welcome to my-gmns-project, a repository for analyzing a large-scale transportation network dataset following the General Modeling Network Specification (GMNS). This README explains how to configure and run the analysis both locally and in the cloud.

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

Recommended: Anaconda Python 3.8+ for easy package management.
2. Create a Virtual Environment:
```python
conda create -n gmns-env python=3.8
conda activate gmns-env
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
!python code/data_cleaning.py
!python code/traffic_assignment.py
```
4. Clone Repo and Run
```python
git clone [https://github.com/yourusername/my-gmns-project](https://github.com/Rising-Stars-by-Sunshine/Jiayang_Hong_PS1).git
cd my-gmns-project
python code/data_cleaning.py
python code/traffic_assignment.py
```
