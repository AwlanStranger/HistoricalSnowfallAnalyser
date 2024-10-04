import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

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

POW_BREAKPOINT = 10 # cm
SEASON_START = 8 # August

dailyDf = pd.DataFrame(data = daily_data)

firstSnowfallFound = False
results = []
for index, row in dailyDf.iterrows():
  if row.date.month == SEASON_START:
    firstSnowfallFound = False
  if firstSnowfallFound:
    continue

  if row.snowfall_sum > POW_BREAKPOINT:
    # find the distance from last august 1st to this day
    yearOfLastAugust = row.date.year # what year is last august?
    if row.date.month < 8: yearOfLastAugust = yearOfLastAugust - 1
    lastAugust = date(yearOfLastAugust, 8, 1)
    distanceFromLastAugust = (row.date.date() - lastAugust).days

    # Collect the year, and distance from august in list of results
    results.append([row.date.date(), distanceFromLastAugust])

    firstSnowfallFound = True
    # print("date          : " + str(row.date.date()))
    # print("snowfall (cm) : " + str(row.snowfall_sum))
    # print('-------------------------------------')

yearlyDf = pd.DataFrame(results, columns=['Season first day', 'Distance from August 1st'])
# print(yearlyDf)

plt.figure(figsize=(10, 6))
plt.plot(yearlyDf['Season first day'], yearlyDf['Distance from August 1st'], marker='o', color='blue', linestyle='-', linewidth=2)
plt.title('Distance from August 1st vs Season first day')
plt.xlabel('Season First Days')
plt.ylabel('Distance from August 1st (days)')
plt.axhline(0, color='red', linestyle='--', label='August 1st')  # Add a horizontal line at y=0
plt.grid()
plt.xticks(yearlyDf['Season first day'].unique(), rotation=45)  # Set x-ticks to unique years
plt.legend()
plt.show()