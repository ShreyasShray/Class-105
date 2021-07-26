import csv
import pandas as pd
import plotly.express as px

with open("class1.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total_marks = 0
n = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks/n

print("Mean is " + str(mean))

df = pd.read_csv("class1.csv")

fig = px.scatter(df, x = "Student Number", y = "Marks", title = "Class 1")

fig.update_layout(shapes = [dict(type = "line", y0 = mean, y1 = mean, x0 = 0, x1 = n)])
fig.update_yaxes(rangemode = "tozero")
fig.show()