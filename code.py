import pandas as pa
import plotly.express as px
import plotly.figure_factory as pf

df = pa.read_csv("data 2.csv")
fig = pf.create_distplot([df["Avg Rating"].tolist()],["Average Rating"],show_hist=False)
fig.show()