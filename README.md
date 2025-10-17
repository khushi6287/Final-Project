# Final-Project
# Indian Road Accidents Analysis

## Project Overview
This project analyzes road accident data in India from 2018 to 2022 using Python. The goal is to explore trends, identify high-risk states, and analyze fatality rates. The analysis includes data visualization, correlation analysis, and computation of yearly accident growth rates.

---

## Features
- Load and inspect road accident dataset.
- Display summary statistics and basic dataset information.
- Analyze total accidents by year.
- Identify top 5 states with the highest number of accidents.
- Calculate and visualize average fatality rate over years.
- Perform correlation analysis between total accidents, fatal accidents, deaths, and injuries.
- Compute year-to-year accident growth rates using NumPy.
- Generate clear visualizations using Matplotlib.

---

## Dataset
- **Filename:** `indian_road_accidents_demo.csv`
- **Columns:**
  - `Year` : Year of data collection (2018–2022)
  - `State/UT` : Name of Indian State or Union Territory
  - `Total_Accidents` : Total number of reported accidents
  - `Fatal_Accidents` : Number of fatal accidents
  - `Deaths` : Total deaths caused by accidents
  - `Injuries` : Total injuries caused by accidents

> Note: Ensure the dataset CSV file is placed in the same directory as the script.

---

## Requirements
- Python 3.x
- Libraries:
  - pandas
  - numpy
  - matplotlib

Install required libraries using:

```bash
pip install pandas numpy matplotlib
