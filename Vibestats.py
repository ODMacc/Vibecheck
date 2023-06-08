import pandas as pd
from datetime import *

class Vibestats:
    def __init__(self):
        self.df = pd.DataFrame(pd.read_csv("history.csv", parse_dates=["Date"], date_format={"Date": "%d/%m/%y"}))
        self.dfav = pd.DataFrame()
        self.dfav["Date"] = self.df["Date"]
        self.dfav["Average Mood"] = self.df["Mood"].rolling(window=7, step=7, min_periods=1).mean()
        self.dfav["Average Energy"] = self.df["Energy"].rolling(window=7, step=7, min_periods=1).mean()
        print(self.dfav)

    def minmaxweek(self, dateinput: datetime, maxormin: str):
        """
        Takes date input and string input
        Finds the week the date input is in and gives data from the Monday of that week as a pandas series
        String input determines whether to return maximum or minimum values of that week
        """
        weekday = dateinput.isocalendar()[2]
        startdate = dateinput - timedelta(days=weekday-1)
        enddate = startdate + timedelta(days=6)
        result = self.df.query('Date >= @startdate & Date <= @enddate')
        weekav = self.dfav.query('Date == @enddate')
        if maxormin == "max":
            return result.max(numeric_only=True)
        else:
            return result.min(numeric_only=True)
    
    def average(self):
        pass