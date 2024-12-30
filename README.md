---
title: "Earthquake Insights Analysis"
output: html_document
---

# Project Overview  
The **Earthquake Insights Analysis** is a comprehensive data visualization and analysis tool designed to provide insights into earthquake activity worldwide. Using cleaned data and interactive visualizations, the project aims to help users understand seismic trends, analyze regions prone to earthquakes, and observe activity patterns based on time, magnitude, and location.

## Table of Contents  
- [Project Overview](#project-overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Technologies Used](#technologies-used)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)  

## Features  
- **Interactive Dashboard**: Built using Python's Shiny framework and Plotly for dynamic, user-friendly data visualizations.  
- **Data Cleaning**: Includes a Jupyter notebook (`quakes-clean.ipynb`) for preprocessing raw earthquake data.  
- **Insights Generation**: Leverages the `quakes-insights.ipynb` notebook to generate insights from the cleaned dataset.  
- **Advanced Visualizations**: Created in `quakes-plots.ipynb`, including bar charts, scatter plots, and heatmaps.  
- **Saved Plots**: Automatically saves plots to the `plots/` directory for easy sharing.  

## Installation  

### Prerequisites  
- Python 3.9+  
- Jupyter Notebook  
- Visual Studio Code  
- Git  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/<your-username>/earthquake-insights.git  
   cd earthquake-insights  
