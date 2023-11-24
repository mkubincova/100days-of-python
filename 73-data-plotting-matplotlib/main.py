import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv', header=0, names=['DATE', 'TAG', 'POSTS'])

# turn date string to date type
df['DATE'] = pd.to_datetime(df['DATE'])

# data manipulation
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df
        # TAG python  c# java ...
# DATE
# 2008-07-01   8     0     1
# 2008-08-01   18    10    3
# ...

# replace NaN with 0
reshaped_df.fillna(0, inplace=True)

# create line chart
# smooth lines by gouping 6 indexs together
roll_df = reshaped_df.rolling(window=6).mean()

# set styling
plt.figure(figsize=(16,7))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# add labels to axis
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)

# set min and max for y-axis
plt.ylim(0, 35000)

# plot line for each column
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)

# add legend to graph
plt.legend(fontsize=16)

# limit rows by daterange
range = (reshaped_df.index > pd.to_datetime('2020-01-01')) & (reshaped_df.index <= pd.to_datetime('2020-12-31'))
new_df = reshaped_df.loc[range]

# or

new_df = reshaped_df.loc['2008-01-01':'2012-12-31']
