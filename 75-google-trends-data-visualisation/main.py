import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv('TESLA Search Trend vs Price.csv')
df_btc_search = pd.read_csv('Bitcoin Search Trend.csv')
df_btc_price = pd.read_csv('Daily Bitcoin Price.csv')
df_unemployment = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')

# table summary
df_tesla.describe()
# 	TSLA_WEB_SEARCH	TSLA_USD_CLOSE
# count	124.000000	124.000000
# mean	8.725806	50.962145
# ...

# check if there are NaN values
df_tesla.isna().values.any()

# count number of NaN values
df_btc_price.isna().values.sum()

# group daily data to month (taking last value for the mont)
df_btc_price_monthly = df_btc_price.resample('M', on='DATE').last()

# DATA VISUALIZATION
# Create locators for ticks on the time axis (big line for years, small for months)
years = mdates.YearLocator()
months = mdates.MonthLocator()
years_fmt = mdates.DateFormatter('%Y')

ax1 = plt.gca()
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

# rotate points on x-axis
plt.xticks(fontsize=14, rotation=45)

# create grid in graph background based on x-axis
ax1.grid(color='lightgrey', linestyle='dashed', linewidth=1)
