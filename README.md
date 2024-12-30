# Project Overview  
The **Earthquake Insights Dashboard** is a comprehensive data visualization and analysis tool designed to provide insights into earthquake activity worldwide. Using cleaned data and interactive visualizations, the project aims to help users understand seismic trends, analyze regions prone to earthquakes, and observe activity patterns based on time, magnitude, and location.

## Table of Contents  
- [Project Overview](#project-overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Technologies Used](#technologies-used)  
- [Author](#author)  

## Features  
- **Interactive Dashboard**: Built using Python's Shiny framework and Plotly for dynamic, user-friendly data visualizations.  
- **Data Cleaning**: Includes a Jupyter notebook (`quakes-clean.ipynb`) for preprocessing raw earthquake data.  
- **Insights Generation**: Leverages the `quakes-insights.ipynb` notebook to generate insights from the cleaned dataset.  
- **Advanced Visualizations**: Created in `quakes-plots.ipynb`, including bar charts, scatter plots, and heatmaps.

## Installation  

### Prerequisites  
- Python 3.9+  
- Jupyter Notebook  
- Visual Studio Code  
- Git  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/<your-username>/earthquake-data-analysis.git  
   cd earthquake-data-analysis  
   ```  

2. Install required Python packages:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. Run the Jupyter notebooks for data cleaning and visualization:  
   ```bash  
   jupyter notebook  
   ```  

4. Start the Shiny dashboard:  
   ```bash  
   python app.py  
   ```  

## Usage  
1. Open the Shiny dashboard in your browser (typically `http://127.0.0.1:8000`).  
2. Navigate through tabs to explore various insights:  
   - **Top 25 Regions with Most Seismic Activity**  
   - **Earthquake Activity by Time of Day**  
   - **Daily Earthquake Activity**  
   - **Top 35 Regions by Average Magnitude**  
   - **Earthquake Activity Heatmap (by Week)**  

## File Structure  

```
earthquake-insights/  
├── app.py                     # Shiny app for interactive dashboard  
├── requirements.txt           # Python dependencies  
├── plots/                     # Saved plots directory  
├── quakes-clean.ipynb         # Data cleaning notebook  
├── quakes-insights.ipynb      # Insights generation notebook  
├── quakes-plots.ipynb         # Visualization notebook  
├── quakes-cleaned.csv         # Cleaned earthquake dataset  
├── LICENSE                    # License file  
└── README.md                  # This file  
```  

## Technologies Used  
- **Python**: Pandas, Plotly, Shiny  
- **Jupyter Notebooks**: For data cleaning, insights, and visualization  
- **Libraries**: NumPy, Plotly, datetime, os  
- **Version Control**: Git and GitHub

## Author  
**Srikar Kalle**  
- GitHub: [Srikar Kalle](https://github.com/srikarsharma16)  
- LinkedIn: [Srikar Kalle](https://www.linkedin.com/in/srikar-kalle-263a10191/)  
```
