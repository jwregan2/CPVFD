import plotly
from plotly.graph_objs import *
# plotly.sign_in(username='cweinschenk', api_key='Ni79tApm5enaARYhUJWY')
import pandas as pd

mapbox_access_token='pk.eyJ1IjoiY3dlaW5zY2hlbmsiLCJhIjoiY2ozd2NyZTRrMDAyNTMyb2h4cmFzOWpwciJ9.NlJ1dlinBVNWsW9FSn1f0w'

df = pd.read_csv('Venues_mod.csv')
df.head()
df['text'] = 'Name: ' + df['Location Name'] + '<br>Style: ' + df['Category'] + '<br>Link: <a href="' + df['Website'] + '"></a>'
limits = [0,100,200,500,1000,20000]
colors = ["rgb(238, 206, 253)","rgb(215, 154, 244)","rgb(191, 96, 235)","rgb(169, 46, 226)","rgb(148, 0, 218)"]

data_split = []
for i in range(len(limits)-1):
    df_sub = df[df['Seated'].between(limits[i],limits[i+1], inclusive=True)]

    data = dict(
        Scattermapbox(
            lat=df_sub['Latitude'],
            lon=df_sub['Longitude'],
            text=df_sub['text'],
            mode='markers',
            marker=dict(
                symbol='circle',
                size=12,
                color = colors[i],
            ),
            name = '{0} - {1}'.format(limits[i],limits[i+1])
        )
    )
    data_split.append(data)

layout = Layout(
    title = 'Seated Capacity of DC Venues<br>(Click legend to toggle capacity ranges)',
    autosize=True,
    showlegend = True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38.92,
            lon=-77.07
        ),
        pitch=0,
        zoom=11
    ),
)

fig = dict(data=data_split, layout=layout )
plotly.offline.plot( fig, validate=False, filename='dc_venues.html' )