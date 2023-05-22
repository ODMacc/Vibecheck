import pandas as pd
import datetime

class Vibestats:
    def __init__(self):
        df = pd.DataFrame(pd.read_csv("history.csv"))
        df["Average Mood"] = df["Mood"].rolling(window=7, step=1, min_periods=1).mean()
        df["Average Energy"] = df["Energy"].rolling(window=7, step=1, min_periods=1).mean()
        print(df)

def minmaxweek():
    dateday = input("Day")
    datemonth = input("Month")