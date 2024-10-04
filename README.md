# Snowfall Analysis Script

This script retrieves historical snowfall data using the Open-Meteo API, processes it to determine the first day of significant snowfall for each winter season, calculates the distance from a seasonal breakpoint to that date, and visualizes the results in a chart.

## Requirements

- **Python** 3.7 or higher
- **Libraries**:
  - `openmeteo_requests`
  - `requests_cache`
  - `pandas`
  - `retry_requests`
  - `matplotlib`
  - `seaborn` (optional for enhanced visuals)

You can install the required libraries using pip:

```
pip install openmeteo_requests requests_cache pandas retry_requests matplotlib seaborn
```

## How It Works

1. **Setup API Client**: The script sets up an Open-Meteo API client with caching and retry functionality.
2. **API Call**: It retrieves daily snowfall data for a specified location and date range.
3. **Data Processing**:
   - It calculates the distance from the seasonal breakpoint for each significant snowfall day found.
   - The script only considers snowfall amounts greater than a defined threshold (e.g., 10 cm).
4. **Data Visualization**: The results are plotted as a line chart showing the distance from the seasonal breakpoint against the first day of snowfall for each season.

## Usage

1. Clone this repository or download the script.
2. Ensure that you have all the required libraries installed.
3. Run the script in your preferred Python environment.
```
python ./index.py
```
Or

```
./index.py
```

## Modifying Parameters

You can modify the following parameters in the script:

- **Location Coordinates**: Change the latitude and longitude in the `params` dictionary to analyze different locations.
- **Date Range**: Adjust the `start_date` and `end_date` in the `params` dictionary to change the timeframe of the data retrieved.
- **Snowfall Threshold**: Modify the `POW_BREAKPOINT` variable to change the minimum snowfall amount to consider significant.

## Output

The script generates a line chart showing the distance from the seasonal breakpoint to the first significant snowfall day for each winter season.

## Why does this matter?

My first real desire to seek out climate knowledge was during the winter of 2023/2024, during the El Nino event. I had just gotten to the rank of "avid" snowboarder when suddenly there was barely any snowfall until January, and even then it was thin sheets of rock-hard ice. My surface level of geography knowledge enough to know what El Nino was but not enough to identify things like "What year is the best to buy a season pass ahead of time?" or "What is the probability opening day at my local hill is on a weekend?" or even "When should I take my PTO for the highest likelihood of aligning with a pow day?". And now we even have to normalize for things like forest fires and global warming affecting the climate. So I set out to make create some tools and study the climate better and make climate studies more accessible to people of all hobbies.

## Acknowledgments

- Open-Meteo API for providing the weather data.
- Matplotlib for data visualization.