import pandas as pd
import plotly.graph_objects as pgo

df = pd.read_csv("data.csv")

allData = df.groupby("level")["attempt"].mean()

graph = pgo.Figure(pgo.Bar(x=["Level 1", "Level 2", "Level 3", "Level 4"],y=allData))
graph.show()