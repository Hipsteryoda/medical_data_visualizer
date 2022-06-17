import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
wt_array = df.weight.to_numpy()
ht_array = df.height.to_numpy()
bmi = wt_array/((ht_array/100)**2)
# multiplying 1 times an array of boolian values converts it to 1's and 0's
df['overweight'] = 1*(bmi > 25)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
chol_array = df.cholesterol.to_numpy()
gluc_array = df.gluc.to_numpy()

df['cholesterol'] = (chol_array > 1)*1
df['gluc'] = (gluc_array > 1)*1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat.sort_values('variable', inplace=True)

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count')
    fig.set_axis_labels('variable', 'total')
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo']<=df['ap_hi']) &
  (df['height'] >= df['height'].quantile(0.025))&
  (df['height'] <= df['height'].quantile(0.975))&
  (df['weight'] >= df['weight'].quantile(0.025))&
  (df['weight'] <= df['weight'].quantile(0.975))
  ]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = mask = np.triu(np.ones_like(corr))



  # Set up the matplotlib figure
  fig, ax = plt.subplots(1, 1, figsize=(12, 12))

  # Draw the heatmap with 'sns.heatmap()'
  ax = sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', cmap='icefire')

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
