# Snowfall Analysis Script

This script retrieves historical snowfall data using the Open-Meteo API, processes it to determine the first day of significant snowfall for each winter season, calculates the distance from August 1st to that date, and visualizes the results in a chart.

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
   - It calculates the distance from the last August 1st for each significant snowfall day found.
   - The script only considers snowfall amounts greater than a defined threshold (e.g., 10 cm).
4. **Data Visualization**: The results are plotted as a line chart showing the distance from August 1st against the first day of snowfall for each season.

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

The script generates a line chart showing the distance from August 1st to the first significant snowfall day for each winter season.

## Acknowledgments

- Open-Meteo API for providing the weather data.
- Matplotlib for data visualization.