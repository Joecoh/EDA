# read this comment first before your delete it!!

#pip install plotly before you run else it wont run 
import pandas as pd
import plotly.express as px

data = {
    'City': ['Chennai', 'Mumbai', 'Delhi', 'Kolkata', 'Bengaluru', 'Hyderabad'],
    'Latitude': [13.08, 19.07, 28.61, 22.57, 12.97, 17.38],
    'Longitude': [80.27, 72.88, 77.20, 88.36, 77.59, 78.48],
    'Temperature': [34, 32, 30, 31, 29, 33]
}

df = pd.DataFrame(data)
print("=== CITY TEMPERATURE DATA ===")
print(df, "\n")

#  Create interactive map
fig = px.scatter_mapbox(
    df,
    lat='Latitude',
    lon='Longitude',
    size='Temperature',          
    color='Temperature',         
    hover_name='City',           
    hover_data={'Temperature': True, 'Latitude': False, 'Longitude': False},
    color_continuous_scale='OrRd',
    zoom=4,
    height=500,
    title='Average Temperature Across Indian Cities'
)

#  Use OpenStreetMap style (free & no API key needed)
fig.update_layout(mapbox_style='open-street-map')

fig.show()
