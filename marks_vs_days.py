import csv
import numpy as np


def getDataSource(data_path):
    days = []
    marks = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))

    return {"x" : marks, "y": days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between number of days for preparation and marks earned by student:  \n--->",correlation[0,1])

def setup():
    data_path  = r"C:\Users\bhuvi\Google Drive\Code\Python\Class 106 - Corelation\data\Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
