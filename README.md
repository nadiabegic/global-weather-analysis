# 🌧️ Global Weather Analysis 
A data-driven investigation into whether London is really “that rainy.”
This project is an adapted version of coursework completed for LSE DS105A.

**AUTHOR:** @nadiabegic on GitHub

![alt text](figures/hq720.png)

[Via Watched Walker on YouTube](https://www.youtube.com/watch?v=H43glfbQEh4)

## 📌 Objective
This repository was commissioned to answer the following question:

_"Is London really as rainy as the movies make it out to be?"_

## 🧠 Statement of Need
London’s “rainy city” reputation is often overstated. While annual precipitation is moderate compared to other capitals, factors such as frequency, variability, and distribution may create the perception of constant drizzle. It is also important to consider the impact of climate change on rainfall, and we should consider that perhaps London was indeed a much rainier city twenty years ago.

This project uses the Open-Meteo Historical Weather API to collect consistent cross-city weather data and visualises how London compares with cities including Amsterdam, Edinburgh, Sarajevo, Madrid, New York, and Dubai.

## 📊 Summary of findings
- London receives less total rainfall than wetter capitals like Amsterdam and Edinburgh.

- However, London experiences a high number of rainy days, contributing to the perception of constant rain.

- Daily precipitation is highly variable, shown in the skewed boxplots, reinforcing expectations of unpredictable weather.

- Climate trends: London had lower total precipitation in 2003 but maintained the same rainy reputation—suggesting cultural perception plays a role.

Full interpretations are provided at the end of `NB02 – Data Analysis.ipynb`.

## 🔧 Methodology
### 1. Data Collection

Cities analysed:
- London
- Edinburgh
- Sarajevo
- Paris
- Madrid
- New York City
- Dubai
- Los Angeles
- Damascus
- Amsterdam

Using the Open-Meteo API, the following were collected for 2003 and 2023:
- Number of rainy days
- Total annual precipitation
- Daily precipitation values

### 2. Data Processing
- Parsed JSON responses into structured data
- Cleaned and validated variables
- Combined metrics across years and cities

### 3. Visualisation

Using lets-plot and GeoPandas:
- Comparative bar charts (2003 vs 2023)
- Boxplots showing precipitation distributions
- A world map highlighting precipitation differences

## 🚀 Implementation and Usage

### How to recreate the Python environment:
Create the virtual environment in the terminal: `python -m venv venv`
Activate the virtual environment: `source venv/bin/activate`
Install the necessary packages from the `requirements.txt` file: `pip install -r requirements.txt`

### How to run the code:
Located in the data folder, the world_cities.csv can be found which was downloaded from the [joelacus/world-cities](https://github.com/joelacus/world-cities/blob/main/world_cities.csv) repository.

1. Begin with `NB01 - Data Collection.ipynb` in the `code` folder and run each code cell in order. This should create six JSON files in the `data` folder each storing different data concerned with precipitation and the number of days of rain in the ten cities selected above. 
2. Repeat the process with `NB02 - Data Analysis.ipynb` to visualise the data. 

## 📁 Repository Structure
```
Global Weather Analysis/
│
├── code/
│   ├── NB01 - Data Collection.ipynb
│   └── NB02 - Data Analysis.ipynb
│
├── data/
│   └── world_cities.csv
│
├── figures/
│   ├── days_rain_plot.png
│   ├── hq720.png
│   ├── total_prec_map.png
│   └── total_prec_plot.png
│
├── .gitignore
├── requirements.txt
└── README.md
```
## Sources:
- [Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api#latitude=51.5085&longitude=-0.1257&start_date=2023-01-01&end_date=2023-12-31&hourly=&daily=rain_sum)
- [Busting the myth of London being a Rainy city](https://stephenliddell.co.uk/2018/01/27/busting-the-myth-of-london-being-a-rainy-city/) 
- [List of cities by average precipitation - Wikipedia](https://en.wikipedia.org/wiki/List_of_cities_by_average_precipitation)
- [What are the most effective ways to visualize weather data?](https://medium.com/@MoonlightO2/what-are-the-most-effective-ways-to-visualize-weather-data-b0d8da8cd62e#:~:text=Choosing%20the%20right%20type%20of,like%20wind%20speed%20or%20humidity)
- [geom_bar - Lets_Plot for Python](https://lets-plot.org/python/pages/api/lets_plot.geom_bar.html#lets_plot.geom_bar)
- [scale_fill_brewer -- Lets_Plot for Python](https://lets-plot.org/python/pages/api/lets_plot.scale_fill_brewer.html)
- [Using Lets-Plot with GeoPandas to Create Maps](https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/cookbook/geopandas_naturalearth.ipynb)
- [Natural Earth data](https://github.com/JetBrains/lets-plot-docs/tree/master/data/naturalearth/admin_0_countries)
