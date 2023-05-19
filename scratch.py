import pandas as pd
import datetime
import random

df = pd.DataFrame(columns=["Date", "Mood", "Energy"])
dict1 = {
}

date = datetime.date(2023, 5, 1)
for ddummy in range(32):
    dict1.update({"Date" : date, "Mood" : random.randrange(1,11), "Energy" : random.randrange(1,11)})
    date += datetime.timedelta(days=1)
    df1 = pd.DataFrame(dict1, index=[0])
    df = pd.concat([df, df1], ignore_index=True)
    print(df)
    print("***")

print(df)
print("Average Mood = " + str((df["Mood"].mean())))
print("Average Energy = " + str(df["Energy"].mean()))