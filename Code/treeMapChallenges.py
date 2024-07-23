# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 08:42:21 2024

@author: tom
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.colors as colors

# Load the data
df = pd.read_csv('~/.spyder-py3/datasetfunds_updated.csv')

# Group by category and calculate metrics
category_data = df.groupby('category').agg({
    'status': lambda x: (x == 'FUNDED').mean(),
    'requested amount': 'sum',
    'fund': lambda x: x.mode().iloc[0]  # Most common fund for this category
}).reset_index()

# Rename columns for clarity
category_data.columns = ['category', 'funded_ratio', 'total_requested', 'primary_fund']

# Create a color scale for funds
unique_funds = sorted(df['fund'].unique(), key=lambda x: int(x.replace('Fund', '')))
color_scale = colors.qualitative.Plotly[:len(unique_funds)]
fund_colors = dict(zip(unique_funds, color_scale))

# Create the treemap
fig = go.Figure(go.Treemap(
    labels=category_data['category'],
    parents=[''] * len(category_data),
    values=category_data['total_requested'],
    textinfo='label+value+percent parent',
    hovertemplate='<b>%{label}</b><br>Total Requested: $%{value:,.0f}<br>Funded Ratio: %{customdata[0]:.2%}<br>Primary Fund: %{customdata[1]}',
    customdata=category_data[['funded_ratio', 'primary_fund']],
    marker=dict(
        colors=[fund_colors[fund] for fund in category_data['primary_fund']],
        colorscale='Viridis',
        showscale=False
    ),
))

# Update layout
fig.update_layout(
    title='Funding Categories TreeMap',
    width=1200,
    height=800,
)

# Add a color legend
for fund, color in fund_colors.items():
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(size=10, color=color),
        showlegend=True,
        name=fund
    ))

# Save the plot as an HTML file
fig.write_html("category_funding_treemap.html")

print("TreeMap has been saved as 'category_funding_treemap.html'.")

# Print some summary statistics
print(category_data.sort_values('total_requested', ascending=False).head(10))