import pandas as pd
import plotly.express as px

df_apps = pd.read_csv('apps.csv')

# Show numeric output in decimal format e.g., 2.15
pd.options.display.float_format = '{:,.2f}'.format

# get 5 random rows
df_apps.sample(n=5)

# delete columns
df_apps = df_apps.drop(columns=['Last_Updated', 'Android_Ver'])

# find and remove NaN
df_apps_clean = df_apps.dropna()
df_apps_clean.isna().values.sum() #0

# find and remove duplicates
df_apps_clean.duplicated().values.sum() #456
df_apps_clean = df_apps_clean.drop_duplicates(subset=['App', 'Type', 'Price'])

# get number of rows per rating
ratings = df_apps_clean['Content_Rating'].value_counts()
# Everyone           6621
# Teen                912
# Mature 17+          357
# Everyone 10+        305
# Adults only 18+       3
# Unrated               1

# PIE chart
fig = px.pie(labels=ratings.index, values=ratings.values, names=ratings.index, title='Content Rating')
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.show()

# DONUT chart
fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             hole=0.6,
             )
fig.update_traces(textposition='inside', textfont_size=15, textinfo='percent')
fig.show()

# check column data types
df_apps_clean.dtypes

# turn 500,000,000 into number
df_apps_clean['Installs'] = df_apps_clean['Installs'].astype(str).str.replace(',', '')
df_apps_clean['Installs'] = pd.to_numeric(df_apps_clean['Installs'])

# create new column by multiplying two col values
df_apps_clean['Revenue_Estimate'] = df_apps_clean['Installs'].mul(df_apps_clean['Price'])

# SCATTER chart
category_installs = df_apps_clean.groupby('Category').agg({'Installs': pd.Series.sum})
category_installs.sort_values('Installs', ascending=True, inplace=True)

cat_number = df_apps_clean.groupby('Category').agg({'App': pd.Series.count})

cat_merged_df = pd.merge(cat_number, category_installs, on='Category', how='inner')
cat_merged_df.sort_values('Installs', ascending=False)

scatter = px.scatter(cat_merged_df,  # data
                     x='App',  # column name
                     y='Installs',
                     title='Category Concentration',
                     size='App',
                     hover_name=cat_merged_df.index,
                     color='Installs')
scatter.update_layout(xaxis_title="Number of Apps (Lower=More Concentrated)",
                      yaxis_title="Installs",
                      yaxis=dict(type='log'))
scatter.show()

# Split the strings on the semi-colon and then .stack them.
stack = df_apps_clean['Genres'].str.split(';', expand=True).stack()
print(f'We now have a single column with shape: {stack.shape}')
# We now have a single column with shape: (8564,)

num_genres = stack.value_counts()
print(f'Number of genres: {len(num_genres)}')
# Number of genres: 53

# BAR chart
bar = px.bar(x=num_genres.index[:15],  # index = category name
             y=num_genres.values[:15],  # count
             title='Top Genres',
             hover_name=num_genres.index[:15],
             color=num_genres.values[:15],
             color_continuous_scale='Agsunset')
bar.update_layout(xaxis_title='Genre',
                  yaxis_title='Number of Apps',
                  coloraxis_showscale=False)
bar.show()

# GROUPED BAR chart
df_free_vs_paid = df_apps_clean.groupby(["Category", "Type"], as_index=False).agg({'App': pd.Series.count})

g_bar = px.bar(df_free_vs_paid,
               x='Category',
               y='App',
               title='Free vs Paid Apps by Category',
               color='Type',
               barmode='group')
g_bar.update_layout(xaxis_title='Category',
                    yaxis_title='Number of Apps',
                    xaxis={'categoryorder': 'total descending'},
                    yaxis=dict(type='log'))
g_bar.show()

# BOX chart
box = px.box(df_apps_clean,
             y='Installs',
             x='Type',
             color='Type',
             notched=True,
             points='all',
             title='How Many Downloads are Paid Apps Giving Up?')
box.update_layout(yaxis=dict(type='log'))
box.show()


df_paid_apps = df_apps_clean[df_apps_clean['Type'] == 'Paid']
box = px.box(df_paid_apps,
             x='Category',
             y='Revenue_Estimate',
             title='How Much Can Paid Apps Earn?')
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Ballpark Revenue',
                  xaxis={'categoryorder': 'min ascending'},
                  yaxis=dict(type='log'))
box.show()


box = px.box(df_paid_apps,
             x='Category',
             y="Price",
             title='Price per Category')
box.update_layout(xaxis_title='Category',
                  yaxis_title='Paid App Price',
                  xaxis={'categoryorder': 'max descending'},
                  yaxis=dict(type='log'))
box.show()
