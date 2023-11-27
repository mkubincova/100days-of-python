import pandas as pd
import matplotlib.pyplot as plt

df_colors = pd.read_csv('data/colors.csv')
df_sets = pd.read_csv('data/sets.csv')
df_themes = pd.read_csv('data/themes.csv')


# find number of uniques values per columns
df_colors.nunique()
# id          135
# name        135
# rgb         124
# is_trans      2


# find number for each value in a column
df_colors['is_trans'].value_counts()
# f    107
# t     28

df_colors.groupby('is_trans').count()
# 	        id	name	rgb
# is_trans
# f	        107	107	107
# t	        28	28	28


# find by column value
df_first_year = df_sets[df_sets['year'] == 1949]


# count number of unique themes per year + rename column
sets_by_year = df_sets.groupby('year').count()
# 	    set_num	    name	theme_id	num_parts
# year
# 1949	    5	    5	        5	        5
# 1950	    6	    6	        6	        6
# 1953	    4	    4	        4	        4

themes_by_year = df_sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)
# 	    nr_themes
# year
# 1949	    2
# 1950	    1
# 1953	    2


# create line graph with multiple y-axis values (Num. sets - left, Num. themes - right)
ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='b')

ax1.set_xlabel('Year')
ax1.set_ylabel('Number of sets', color='g')
ax2.set_ylabel('Number of themes', color='b')


# merge tables with foreign id
set_theme_count = df_sets.theme_id.value_counts()
set_theme_count = pd.DataFrame({'id': set_theme_count.index, 'set_count': set_theme_count.values})
#   id	set_count
# 0	158	    753
# 1	501	    656
# 2	494	    398

df_merged = pd.merge(set_theme_count, df_themes, on='id')
# 	id	set_count	name	parent_id
# 0	158	    753	    Star Wars	NaN
# 1	501	    656	    Gear	    NaN
# 2	494	    398	    Friends	    NaN

