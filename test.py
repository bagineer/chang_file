import pandas as pd
from tkinter import filedialog
import tkinter as tk
import math

# file = filedialog.askopenfilename(initialdir = '/', title = 'select a file',
#                                   filetypes = (("Microsoft Excel 워크시트", "*.xlsx"), ("all files", "*.*")))
file = 'C:/Users/BIH/Desktop/test/노원사진양식_2020.xlsx'
# root = tk.Tk()

print(file)

df = pd.read_excel(file, sheet_name = 'Sheet1')
# print(df.head(5)) # head (5 rows)

# print(df.axes)    # attributes

# print(df.iloc[0, :10])  # range [rows, columns]
#
# print(df.iloc[:, 3:5])    # start, end date
# print(df.loc[1:2])    # select row by index from 1 to 2

print(df)

print("===========================")

# indexes = []
#
# for c in set(df['category']):
#     if not pd.isnull(c):
#         indexes.append((df[df['category'] == c].index[0], c))
#
# indexes.sort()
# print(indexes)
#
# for i in range(len(indexes) - 1):
#     cnt = indexes[i+1][0] - indexes[i][0]
#     print(indexes[i], cnt)


for c in set(df['category']):
    if not pd.isnull(c):
        st_idx = df[df['category'] == c].index[0]
        print(st_idx, c)
        idx =  st_idx
        cnt = 1
        while True:
            # Todo
            sets = int(df.iloc[idx, 2])
            st_date = df.iloc[idx, 3]
            ed_date = df.iloc[idx, 4]
            print(sets, st_date, ed_date)

            for i in range(sets):
                print("k", end = '')
            idx += 1
            if idx == df.shape[0]:
                break
            if not pd.isnull(df['category'][idx]):
                break
        print()

print(df.shape[0])
# print("===============")
print(set(df['category']))
# print(set(df['item']))


# root.mainloop()