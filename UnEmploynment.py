import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv(r'C:\Users\sheel\Desktop\Ceiling-Zero\April_unemploynment.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['unemp'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Blues',
    colorbar_title = "Unemploynment %"
))

fig.update_layout(
    title_text = 'April 2020 unemploynment data',
    geo_scope='usa')

fig.show()