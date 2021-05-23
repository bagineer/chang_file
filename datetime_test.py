from datetime import datetime
import piexif
import pandas as pd
import time

from pandas._libs.tslibs.timestamps import Timestamp
ts = Timestamp('2018-12-01 00:00:00', freq='MS')
date_time = ts.to_pydatetime()
print(ts, type(ts))
print(date_time, type(date_time))

filename = 'C:/Users/BIH/Downloads/32413241234.jpg'
exif_dict = piexif.load(filename)

# cpt_time = "2020-10-30 00:00:00"
cpt_time = datetime.strptime("2020-10-30 00:00:00", "%Y-%m-%d %H:%M:%S").strftime("%Y:%m:%d %H:%M:%S")
print(cpt_time, type(cpt_time))


new_date = datetime(2000, 12, 20, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")    # 찍은 날짜
print(new_date, type(new_date))

stamp = pd.Timestamp(2019, 12, 22, 13, 30, 59)
new_stamp = stamp.to_pydatetime()
print("***", new_stamp, type(new_stamp))


crtDate = datetime(2018, 12, 25, 0, 0, 0)   # 만든 날짜
crtTime = int(time.mktime(crtDate.timetuple()))
print(crtTime, type(crtTime))