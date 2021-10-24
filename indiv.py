import pandas as pd
import os
import plotly.graph_objects as pgo
os.system("cls")

student = input("Enter id: ")

df = pd.read_csv("data.csv")

studentDF = df.loc[df['student_id']==student]

allStuData = studentDF.groupby("level")["attempt"].mean()

graph = pgo.Figure(pgo.Bar(x=["Level 1", "Level 2", "Level 3", "Level 4"],y=allStuData))
graph.show()
print(allStuData)