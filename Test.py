import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv(r'C:\Users\sheel\Desktop\Ceiling-Zero\April_unemploynment.csv')
dg = pd.read_csv(r'C:\Users\sheel\Desktop\Ceiling-Zero\Covid.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z = df['unemp'].astype(float),
    locationmode = 'USA-states',
    colorscale = 'Reds',
    colorbar_title = "Unemploynment %",
))


sig = go.Figure(data=go.Choropleth(
    locations=dg['Code'],
    z = dg['Case'].astype(int),
    locationmode = 'USA-states',
    colorscale = 'Blues',
    colorbar_title = "Covid Cases %"
))


fig.update_layout(
    title_text = 'April 2020 Unemploynment data',
    geo_scope='usa', # limite map scope to USA
)


sig.update_layout(
    title_text = 'April 2020 Covid Cases data',
    geo_scope='usa')


fig.show()
sig.show()

#plots = [fig.show(),sig.show()]

