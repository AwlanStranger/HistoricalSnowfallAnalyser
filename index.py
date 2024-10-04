import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 44.5011,
	"longitude": -80.3161,
	"start_date": "1950-09-01",
	"end_date": "2024-06-30",
	"daily": "snowfall_sum",
	"timezone": "America/New_York"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_snowfall_sum = daily.Variables(0).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["snowfall_sum"] = daily_snowfall_sum

POW_BREAKPOINT = 3 # cm
SEASON_START = 8 # August

df = pd.DataFrame(data = daily_data)
# print(df.iloc[0].date.month)

firstSnowfallFound = False
for index, row in df.iterrows():
  if df.iloc[index].date.month == SEASON_START:
    firstSnowfallFound = False
  if firstSnowfallFound:
    continue

  if df.iloc[index].snowfall_sum > POW_BREAKPOINT:
    print("date          : " + str(df.iloc[index].date.date()))
    print("snowfall (cm) : " + str(df.iloc[index].snowfall_sum))
    print('-------------------------------------')
    firstSnowfallFound = True