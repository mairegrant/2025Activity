import plotly.express as px
import pandas as pd

df = pd.read_csv("longLat2.csv")

df.dropna(
    axis=0,
  #  how='any',
   # thresh=None,
    subset=None,
    inplace=True
)

color_scale = [(0, 'pink'), (1, 'red')]

fig = px.scatter_mapbox(df,
                        lat="Long",
                        lon="Lat",
                        # hover_name="Address",
                        #  hover_data=["Address", "Listed"],
                        color="Lat",
                        color_continuous_scale=color_scale,
                        size="Long",
                        zoom=8,
                        height=800,
                        width=800)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
