import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')

# print first/last 5 rows of dataframe
df.head()
df.tail()

# print number of rows and columns
df.shape

# print column names
df.columns

# check for NaN fields (returns True/False)
df.isna()

# create df without NaN
clean_df = df.dropna()

# get values:
clean_df['Starting Median Salary'].max() #max value
clean_df['Starting Median Salary'].idxmax() #id of max value

clean_df['Starting Median Salary'].min() #min value
clean_df['Starting Median Salary'].idxmin() #id of min value

clean_df['Undergraduate Major'][8] #value of column ['Undergraduate Major'] in row 8

# calc difference between two columns and save it to new column in the df
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(1, 'Spread', spread_col)
clean_df.head()

# sort values by column
low_risk = clean_df.sort_values('Spread')
high_risk = clean_df.sort_values('Spread', ascending=False)

# group by column values
groups = clean_df.groupby('Group') #STEM, HASS, Business
groups.count()
groups.mean()

# set formatting
pd.options.display.float_format = '{:,.2f}'.format # 123,545.25

# copy table from a website and adjust column names
table_from_html = pd.read_html("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")
df = table_from_html[0].copy()
df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]

# add tables from other pages to main dataframe
for page_no in range(2, 35):
    table_from_html = pd.read_html(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page_no}")
    page_df = table_from_html[0].copy()
    page_df.columns = ["Rank", "Major", "Type", "EarlyCareerPay", "MidCareerPay", "HighMeaning"]
    df = df.concat(page_df, ignore_index=True)

# remove unnecessary columns
df = df[["Major", "EarlyCareerPay", "MidCareerPay"]]

# clean columns
df.replace({"^Major:": "", "^Early Career Pay:\$": "", "^Mid-Career Pay:\$": "", ",": ""}, regex=True, inplace=True)
# change datatype of numeric columns
df[["EarlyCareerPay", "MidCareerPay"]] = df[["EarlyCareerPay", "MidCareerPay"]].apply(pd.to_numeric)

