# DS105 Week 6 Summative 🌧️

## Objective:
This repository was commissioned by the Office of Quirky Inquiries (OQI) to answer the following research question:

_"Is London really as rainy as the movies make it out to be?"_

## Statement of Need:
The question of the extent of London's 'raininess' is crucial to answer, as Londoners have been enabled to complain about their weather for far too long. The answer to this perplexing question warrants deeper investigation than simply the annual precipitation that London faces compared to other cities; there are various factors that contribute to one's perception of 'raininess'. This repository was developed to assess the variables of total precipitation, number of days of rain, and daily precipitation in 2023. However, it is also important to consider the impact of time and climate change on rainfall, and we should consider that perhaps London was indeed a much rainier city twenty years ago. Thus, we also obtain and visualise the three variables mentioned above in 2003. The OpenMeteo API will provide us with a variety of historical weather data to be used in this data collection and analysis. 

## Summary of findings:
There are numerous variables that contribute towards the perception that London is a rainy city. London does not rain nearly as much as some of the rainiest capital cities in Europe (e.g. Amsterdam, Edinburgh) as revealed by the bar chart and world map depicting the total precipitation, however there are factors that contribute to the myth of London being a rainy city. London has a relatively high number of days of rain in year depicted by the bar chart, and it has some unpredictable weather as demonstrated by the skewness of the boxplot. London received less rainfall 20 years ago than it does now, yet it held the same reputation then. Ultimately, it's complicated. More details of the results may be found at the bottom of NB02.  

## Methodology:
1. Obtain the longitude and latitude of the following ten different cities:
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

2. Calculate the number of days of rain in 2003 and 2023 of each city
3. Obtain the total precipitation in mm in 2003 and 2023 of each city
4. Obtain the daily precipitation in mm in 2003 and 2023 of each city
5. Visualise the data using the lets-plot library
    - The number of days of rain in 2003 and 2023 will be displayed on a single bar chart
    - The total precipitation in 2003 and 2023 will also be displayed on a single bar chart and an interactive world map created with geopandas
    - The distribution of precipitation in 2003 and 2023 will each be represented with ten boxplots (one for each city)

## Implementation and usage:
A user will first need to install the following:
- pandas

```bash
conda install anaconda::pandas 
```

- requests

```bash
conda install anaconda::requests
```

- lets_plot

```bash
pip install lets-plot
```

- geopandas

```bash
conda install geopandas
```

- shapefile

```bash
conda install anaconda::pyshp
```

- shapely

```bash
conda install conda-forge::shapely
```

Located in the data folder, the world_cities.csv can be found which was downloaded from the [joelacus/world-cities](https://github.com/joelacus/world-cities/blob/main/world_cities.csv) repository.

Begin with _NB01 - Data Collection.ipynb_ in the _code_ folder and run each code cell in order. This should create six JSON files in the _data_ folder each storing different data concerned with precipitation and the number of days of rain in the ten cities selected above. Then repeat the process with _NB02 - Data Analysis.ipynb_ to visualise the data. 

## Use of AI:
ChatGPT was used in this project to assist in combatting errors. The link to the chat can be found [here](https://chatgpt.com/share/6734e33b-8c20-8000-ae9b-4dc765ff37ae).

## Sources:
- https://open-meteo.com/en/docs/historical-weather-api#latitude=51.5085&longitude=-0.1257&start_date=2023-01-01&end_date=2023-12-31&hourly=&daily=rain_sum
- https://stephenliddell.co.uk/2018/01/27/busting-the-myth-of-london-being-a-rainy-city/ 
- https://en.wikipedia.org/wiki/List_of_cities_by_average_precipitation
- https://medium.com/@MoonlightO2/what-are-the-most-effective-ways-to-visualize-weather-data-b0d8da8cd62e#:~:text=Choosing%20the%20right%20type%20of,like%20wind%20speed%20or%20humidity
- https://lets-plot.org/python/pages/api/lets_plot.geom_bar.html#lets_plot.geom_bar
- https://lets-plot.org/python/pages/api/lets_plot.scale_fill_brewer.html
- https://nbviewer.org/github/JetBrains/lets-plot-docs/blob/master/source/examples/cookbook/geopandas_naturalearth.ipynb
- https://github.com/JetBrains/lets-plot-docs/tree/master/data/naturalearth/admin_0_countries
