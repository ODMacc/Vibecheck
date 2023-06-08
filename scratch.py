import pandas as pd
from datetime import *
from random import *

date_one = datetime(2023,4,30)
date_gen = lambda x: date_one + timedelta(days=x)
mood_gen = lambda: randint(1,10)
enrg_gen = lambda: randint(1,10)

dict_list = []

for x in range(1,32):
    new_date = date_gen(x)
    dict_list.append(
        {
            "Date": new_date,
            "Mood": mood_gen(),
            "Energy": enrg_gen()
        }
    )

df = pd.DataFrame(dict_list)


dateinput = pd.to_datetime("19/5/2023", dayfirst=True)

weekday = dateinput.isocalendar()[2]
startdate = dateinput - timedelta(days=weekday-1)
enddate = startdate + timedelta(days=6)
result = df.query('Date >= @startdate & Date <= @enddate')
print(type(result))