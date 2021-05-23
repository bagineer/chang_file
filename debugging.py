"""
# from tkinter import *
#
# window = Tk()
# window.geometry('{}x{}'.format(300, 200))
#
# window.grid_columnconfigure(0, weight = 2)
# window.grid_columnconfigure(1, weight = 1)
# window.grid_rowconfigure(0, weight = 1)
#
# f1 = Frame(window, bg = 'red')
# f1.grid(row = 0, column = 0, sticky = 'nesw')
# f2 = Frame(window, bg = 'blue')
# f2.grid(row = 0, column = 1, sticky = 'nesw')
#
# window.mainloop()
"""


"""
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open("C:/Users/BIH/Downloads/20201030_085952.jpg")
info = img.getexif()

taglabel = {}

for tag, value in info.items():
    decoded = TAGS.get(tag, tag)
    TAGS.get()
    taglabel[decoded] = value



print(taglabel)

print(taglabel['DateTimeOriginal'])
print(taglabel['DateTimeDigitized'])
print(taglabel['DateTime'])

taglabel['DateTimeOriginal'] = '2020:10:01 08:59:52'
# taglabel['DateTimeDigitized'] = '2020:10:01 08:59:52'

print(taglabel['DateTimeOriginal'])
print(taglabel['DateTimeDigitized'])



img.close()
"""


from datetime import datetime
import piexif
import os
import time

filename = 'C:/Users/BIH/Desktop/tmp/2호기_커튼월_1_2.jpg'
exif_dict = piexif.load(filename)
# new_date = datetime(2018, 1, 1, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
# exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
# exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
# exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
# exif_bytes = piexif.dump(exif_dict)
# piexif.insert(exif_bytes, filename)

# print(exif_dict['0th'])
# print(piexif.ImageIFD.DateTime)
# print(piexif.TAGS['Image'][306])
# print(exif_dict['Exif'][piexif.ImageIFD.DateTimeOriginal])

# DateTimeOriginal : 찍은 날짜
# os.utime : (액세스한 날짜, 수정한 날짜)


# offsetDate = datetime(100, 1, 1, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
# offsetOrgDate = datetime(10, 1, 2, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
# offsetDigitDate = datetime(150, 1, 3, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")

new_date = datetime(2021, 5, 18, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")    # 찍은 날짜
# new_date = datetime("2020-10-30 00:00:00").strptime("%Y:%m:%d %H:%M:%S")
modDate = datetime(2021, 5, 25, 0, 0, 0)   # 수정한 날짜
modTime = time.mktime(modDate.timetuple())
accDate = datetime(2021, 5, 27, 0, 0, 0)
accTime = time.mktime(accDate.timetuple())

print(new_date)

# exif_dict['Exif'][piexif.ExifIFD.OffsetTime] = offsetDate
# exif_dict['Exif'][piexif.ExifIFD.OffsetTimeOriginal] = offsetOrgDate
# exif_dict['Exif'][piexif.ExifIFD.OffsetTimeDigitized] = offsetDigitDate
exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
# exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date_2


exif_bytes = piexif.dump(exif_dict)
piexif.insert(exif_bytes, filename)


print(exif_dict.keys())
for k in exif_dict.keys():
    print(exif_dict[k])

os.utime(filename, (accTime, modTime))

# d = {1: 3, 'b': 2, 'c':'s'}
# print(d[1])
# print(d['c'])

# Access time in seconds
atime = 200000000

# Modification time in seconds
mtime = 100000000

# Set the access time and
# modification time for the
# above specified path
# using os.utime() method
tup = (accTime, modTime)

print(tup)

import pywintypes, win32file, win32con

def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, wintime, None, None)
    winfile.close()



crtDate = datetime(2021, 5, 18, 0, 0, 0)   # 만든 날짜
crtTime = int(time.mktime(crtDate.timetuple()))

print()


changeFileCreationTime(filename, crtTime)