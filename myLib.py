'''
## Stack class
class Stack:
    def __init__(self):
        self.s = []

    # stack에 item을 추가한다.
    def push(self, item):
        self.s.append(item)

    # stack에서 item을 꺼낸다.
    def pop(self):
        if self.isEmpty() == True:
            return
        else:
            return self.s.pop()

    # stack이 비어있는지 확인한다.
    def isEmpty(self):
        if len(self.s) == 0:
            return True
        else:
            return False

    # stack의 마지막 item을 확인한다.
    def peek(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.s[-1]

    # stack의 크기를 반환한다.
    def size(self):
        return len(self.s)

    # stack을 출력한다.
    def print(self):
        print(self.s)


## Node class
class Node:
    def __init__(self, item):
        self.item = item
        self.cNodes = []

    def hasChild(self):
        if len(self.cNodes) > 0:
            return True
        else:
            return False

    def insertChild(self, node):
        self.cNodes.append(node)

    def searchChild(self, node):
        if self.hasChild():
            for _node in self.cNodes:
                if _node == node:
                    idx = self.cNodes.index(_node)
                    break
        else:
            idx = -1
        return idx

    def deleteChild(self, node):
        if self.hasChild():
            idx = self.searchChild(node)
            if idx < 0:
                print("node doesn't exist")
            else:
                print(self.cNodes[idx].item, "has been deleted")
                self.cNodes.pop(idx)
        else:
            print("has no children")

    def printChild(self):
        if self.hasChild():
            for _node in self.cNodes:
                print(_node.item)
        else :
            print("has no children")

## Tree class
class Tree:
    def __init__(self, root):
        self.root = root
'''

import os
import pandas as pd

import piexif
import random
import time

from tkinter import filedialog
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.font as tk_font

import pywintypes, win32file, win32con


## Node class
class Node:
    def __init__(self, item):
        self.item = item
        self.child = []

    def get_item(self):
        return self.item

    def get_size(self):
        return len(self.child)

    def has_child(self):
        if self.get_size() > 0:
            return True
        else:
            return False

    def insert_child(self, node):
        self.child.append(node)

    def search_child(self, node):
        idx = -1
        if self.has_child():
            for _node in self.child:
                if _node == node:
                    idx = self.child.index(_node)
                    break
        return idx

    def delete_child(self, node):
        if self.has_child():
            idx = self.search_child(node)
            if idx < 0:
                print("node doesn't exist")
            else:
                print(self.child[idx].item, "has been deleted")
                self.child.pop(idx)
        else:
            print("has no children")

    def print_child(self):
        if self.has_child():
            for _node in self.child:
                print(_node.item)
        else :
            print("has no children")

    def print(self):
        print(self.item)


## Tree class
class Tree:
    def __init__(self, root):
        self.root = root
        self._make_tree(root)

    def get_root(self):
        return self.root

    def get_root_item(self):
        return self.root.get_item()

    def _make_tree(self, node):
        cur_node = node
        dir_list = os.listdir(cur_node.item)
        for d in dir_list:
            _path = cur_node.item + '/' + d
            if os.path.isdir(_path):
                child = Node(_path)
                cur_node.insert_child(child)
                self._make_tree(child)


class TwL:
    """
    Tree with a List
    """

    def __init__(self, t):
        self.ST_HOUR = 9
        self.ED_HOUR = 17
        self.tree = t
        self.err_list = []
        self.items = []
        self.mode = ''
        self.df = None
        self.prev_dates_1 = dict()
        self.work_dates_1 = dict()
        self.post_dates_1 = dict()
        self.prev_dates_2 = dict()
        self.work_dates_2 = dict()
        self.post_dates_2 = dict()

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def _pre_order(self, node):
        print(node.item)
        for c in node.child:
            self._pre_order(c)

    def get_tree_root(self):
        return self.tree.get_root()

    def get_tree_root_item(self):
        return self.tree.get_root_item()

    def change_file(self, node):
        if not node.has_child():
            _path = node.item
            if '잔여' in _path or '호기' not in _path:
                return
            dirs = _path.split('/')

            for d in dirs:
                if '호기' in d:
                    m = d
            n = dirs[-1]

            if len(n) < 2:
                part = dirs[-2].replace(' ', '_')

                file_list = os.listdir(_path)
                for file in file_list:
                    old_name = _path + '/' + file
                    new_name = _path + '/' + m + '_' + part + '_' + n + '_' + file[-5:]
                    try:
                        os.rename(old_name, new_name)
                    except Exception as err:
                        print(err)
                        if _path not in self.err_list:
                            self.err_list.append(_path)
            else:
                if _path not in self.err_list:
                    self.err_list.append(_path)
        for c in node.child:
            self.change_file(c)

    def clear_err_list(self):
        self.err_list = []

    def set_items(self, node):
        if not node.has_child():
            _path = node.item
            if '잔여' in _path or '호기' not in _path:
                return
            _dirs = _path.split('/')
            part = _dirs[-2]
            if part not in self.items:
                self.items.append(part)
        for c in node.child:
            self.set_items(c)

    def change_crt_time(self, file_name, new_date):
        new_time = int(time.mktime(new_date.timetuple()))
        win_time = pywintypes.Time(new_time)
        win_file = win32file.CreateFile(
            file_name, win32con.GENERIC_WRITE,
            win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
            None, win32con.OPEN_EXISTING,
            win32con.FILE_ATTRIBUTE_NORMAL, None)

        win32file.SetFileTime(win_file, win_time, None, None)
        win_file.close()

    def change_exif(self, node):
        if not node.has_child():
            _path = node.item
            if '잔여' in _path or '호기' not in _path:
                return
            dirs = _path.split("/")

            for d in dirs:
                if '호기' in d:
                    m = d
            part = dirs[-2]
            idx = int(dirs[-1]) - 1

            if m == '1호기':
                prev_date = self.prev_dates_1[part][idx]
                work_date = self.work_dates_1[part][idx]
                post_date = self.post_dates_1[part][idx]
            elif m == '2호기':
                prev_date = self.prev_dates_2[part][idx]
                work_date = self.work_dates_2[part][idx]
                post_date = self.post_dates_2[part][idx]

            # print(part, idx+1, " : ", type(prev_date), prev_date, '/', work_date, '/', post_date)
            # print(m, part, idx+1)

            file_list = os.listdir(_path)

            for file in file_list:
                img = _path + '/' + file
                file_name, _ = file.split('.')

                if file_name[-1] == "1":
                    date = prev_date
                elif file_name[-1] == "2":
                    date = work_date
                elif file_name[-1] == "3":
                    date = post_date

                try:
                    cpt_date = date.strftime("%Y:%m:%d %H:%M:%S")
                    exif_dict = piexif.load(img)
                    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = cpt_date
                    # exif_dict['Exif'][piexif.ExifIFD.OffsetTime] = offsetDate
                    # exif_dict['Exif'][piexif.ExifIFD.OffsetTimeOriginal] = offsetOrgDate
                    # exif_dict['Exif'][piexif.ExifIFD.OffsetTimeDigitized] = offsetDigitDate

                    mod_date = date + pd.Timedelta(days=1)
                    mod_date = mod_date.to_pydatetime()
                    acc_date = mod_date
                    mod_time = time.mktime(mod_date.timetuple())
                    acc_time = time.mktime(acc_date.timetuple())

                    exif_bytes = piexif.dump(exif_dict)
                    piexif.insert(exif_bytes, img)

                    os.utime(img, (acc_time, mod_time))
                    self.change_crt_time(img, date.to_pydatetime())

                    # print(file_name)
                    # print(cpt_date, type(cpt_date))
                    # print(date, type(date))
                    # print(mod_time, mod_date, type(mod_date))
                    # print(acc_time, acc_date, type(acc_date))
                except Exception as err:
                    print(err)
                    if _path not in self.err_list:
                        self.err_list.append(_path)

        for c in node.child:
            self.change_exif(c)

    def set_dates(self, df):
        self.df = df

        for item in self.items:
            if item not in set(self.df['item']):
                continue
            self.prev_dates_1[item] = []
            self.work_dates_1[item] = []
            self.post_dates_1[item] = []
            self.prev_dates_2[item] = []
            self.work_dates_2[item] = []
            self.post_dates_2[item] = []

            row = self.df[self.df['item'] == item].index[0]

            for idx in range(2):
                if idx == 0:
                    col_1, col_2, col_3 = 2, 3, 4
                else:
                    col_1, col_2, col_3 = 2, 8, 9

                sets = int(self.df.iloc[row, col_1])
                st_date = self.df.iloc[row, col_2]
                ed_date = self.df.iloc[row, col_3]

                days = (ed_date - st_date).days + 1

                self.set_prev_post_dates(item, idx, sets)

                if sets % days == 0:
                    for day in range(days):
                        self.set_work_dates(item, idx, sets//days, day)

                        # h, m, s = self.ST_HOUR, random.randint(0, 60), 0
                        # for _ in range(sets // days):
                        #     h += random.randint(1, 3)
                        #     m += random.randint(1, 2)
                        #     s = random.randint(0, 60)
                        #
                        #     if m >= 60:
                        #         m %= 60
                        #         h += 1
                        #
                        #     if h == 12:
                        #         h = 13
                        #     elif h >= 17:
                        #         h = 16
                        #
                        #     work_dates[item].append(st_date + pd.Timedelta(days=j, hours=h, minutes=m, seconds=s))
                else:
                    if sets > days:
                        rem = sets % days
                        for day in range(days):
                            if rem > 0:
                                self.set_work_dates(item, idx, sets//days + 1, day)
                                rem -= 1
                            else:
                                self.set_work_dates(item, idx, sets//days, day)

                            # for _ in range(sets // days):
                            #     work_dates[item].append(st_date + pd.Timedelta(days=day))
                            # if rem > 0:
                            #     work_dates[item].append(st_date + pd.Timedelta(days=day))
                            #     rem -= 1
                    else:
                        for day in range(sets):
                            self.set_work_dates(item, idx, 1, day+1)
                            # work_dates[item].append(st_date + pd.Timedelta(days=day + 1))

    def set_prev_post_dates(self, item, idx, sets):
        if '발판' in item or '비계' in item:
            return

        row = self.df[self.df['item'] == item].index[0]

        if idx == 0:
            col_1, col_2 = 3, 4
            prev_dates = self.prev_dates_1
            post_dates = self.post_dates_1
        elif idx == 1:
            col_1, col_2 = 8, 9
            prev_dates = self.prev_dates_2
            post_dates = self.post_dates_2

        prev = self.df.iloc[row, col_1] - pd.Timedelta(days=1)
        post = self.df.iloc[row, col_2] + pd.Timedelta(days=1)

        for k in range(2):
            h, m = random.randint(9, 15), random.randint(0, 60)
            for _ in range(sets):
                m += random.randint(1, 5)
                s = random.randint(0, 60)

                if m >= 60:
                    m %= 60
                    h += 1

                if h == 12:
                    h += 1
                elif h >= self.ED_HOUR:
                    h = self.ED_HOUR - 1

                if '세척' in item:
                    prev = self.df.iloc[row, col_1]

                if k == 0:
                    prev_dates[item].append(prev + pd.Timedelta(hours=h, minutes=m, seconds=s))
                else:
                    post_dates[item].append(post + pd.Timedelta(hours=h, minutes=m, seconds=s))

    def _plus_time(self, item, h, m):
        if '발판' in item:
            lm, rm = 1, 5
        elif '비계' in item:
            lm, rm = 10, 20
        else:
            lm, rm = 15, 30

        m += random.randint(lm, rm)
        s = random.randint(0, 60)

        if m >= 60:
            m %= 60
            h += 1

        if h == 12:
            h += 1
        elif h >= self.ED_HOUR:
            h = self.ED_HOUR - 1

        return h, m, s

    def set_work_dates(self, item, idx, cnt, day):
        row = self.df[self.df['item'] == item].index[0]

        if idx == 0:
            col = 3
            work_dates = self.work_dates_1
        elif idx == 1:
            col = 8
            work_dates = self.work_dates_2

        st_date = self.df.iloc[row, col]

        if '발판' in item or '비계' in item:
            if '발판' in item:
                h, m = random.randint(9, 15), random.randint(0, 60)
            else:
                h, m = self.ST_HOUR, random.randint(0, 60)

            for _ in range(cnt):
                h, m, s = self._plus_time(item, h, m)
                if idx == 0:
                    self.prev_dates_1[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))
                    h, m, s = self._plus_time(item, h, m)
                    work_dates[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))
                    h, m, s = self._plus_time(item, h, m)
                    self.post_dates_1[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))
                else:
                    self.prev_dates_2[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))
                    h, m, s = self._plus_time(item, h, m)
                    work_dates[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))
                    h, m, s = self._plus_time(item, h, m)
                    self.post_dates_2[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))

        else:
            if '세척' in item:
                st_date = self.df.iloc[row, col] + pd.Timedelta(days=1)
            h, m = self.ST_HOUR, random.randint(0, 60)

            for _ in range(cnt):
                h, m, s = self._plus_time(item, h, m)
                work_dates[item].append(st_date + pd.Timedelta(days=day, hours=h, minutes=m, seconds=s))


class App(Tk):
    def __init__(self, master):
        Tk.__init__(self, master)
        self.master = master
        self.twl = TwL(None)
        self.radVar = StringVar(None, "i")
        self.dir_text = None
        self.file_text = None
        self.state_text = None
        self.err_text = None
        self.file_selected = False
        self.dir_selected = False
        self.initialize()

    def initialize(self):
        # Font
        font = tk_font.Font(size=10, weight='bold')

        # Frames
        frame1 = Frame(self, bg='powderblue')
        frame1.grid(row=0, column=0, padx=5, pady=10, sticky='EW')
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_columnconfigure(1, weight=1)
        frame2 = Frame(self, bg='powderblue')
        frame2.grid(row=1, column=0, padx=5, pady=10, sticky='EW')
        frame2.grid_columnconfigure(1, weight=1)
        frame3 = Frame(self, bg='powderblue')
        frame3.grid(row=2, column=0, padx=5, pady=10, sticky='EW')
        frame3.grid_columnconfigure((0, 1), weight=1)
        frame4 = Frame(self, bg='powderblue')
        frame4.grid(row=3, column=0, padx=5, pady=10, sticky='EW')
        frame4.grid_columnconfigure(0, weight=1)
        frame4_1 = Frame(frame4, bg='powderblue')
        frame4_1.grid(row=1, column=0, sticky='NESW')
        frame4_1.grid_columnconfigure(0, weight=1)

        # Select Mode
        mode_btn_1 = Radiobutton(frame1, text='Interior', value='i', variable=self.radVar,
                                 command=self.select_mode, bg='white', tristatevalue='x')
        mode_btn_1.grid(row=0, column=0, padx=5)
        mode_btn_2 = Radiobutton(frame1, text='Exterior', value='e', variable=self.radVar,
                                 command=self.select_mode, bg='white', tristatevalue='x')
        mode_btn_2.grid(row=0, column=1, padx=5)

        # Select Folder
        dir_sel_btn = Button(frame2, text='Select Folder', command=self.select_dir, bg='white')
        dir_sel_btn.grid(row=0, column=0, sticky='EW')
        self.dir_text = Text(frame2, height=1)
        self.dir_text.grid(row=0, column=1, padx=5, sticky='EW')

        # Select Date File
        date_sel_btn = Button(frame2, text='Select Date File', command=self.select_date_file, bg='white')
        date_sel_btn.grid(row=1, column=0, sticky='EW')

        self.file_text = Text(frame2, height=1)
        self.file_text.grid(row=1, column=1, padx=5, sticky='EW')

        # Change File Names
        name_change_btn = Button(frame3, text='Change Image Name', command=self.change_img_name, bg='white',
                                 width=20, height=2)
        name_change_btn.grid(row=0, column=0)

        date_change_btn = Button(frame3, text="Change Date", command=self.change_date, bg='white',
                                 width=20, height=2)
        date_change_btn.grid(row=0, column=1)

        self.state_text = Text(frame3, height=1, width=30)
        self.state_text.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

        # List of Error Directories
        err_label = Label(frame4, height=1, text='Directories with error', bg='powderblue', font=font)
        err_label.grid(row=0, column=0)
        scroll_bar = Scrollbar(frame4_1, orient=VERTICAL)
        self.err_text = Text(frame4_1, height=10, yscrollcommand=scroll_bar.set)
        self.err_text.grid(row=0, column=0)
        scroll_bar.grid(row=0, column=1, sticky='NS')
        scroll_bar.config(command=self.err_text.yview)

        # Initial values
        self.geometry('{}x{}'.format(600, 400))
        self.title('Shinil_Nowon')
        self.config(bg='powderblue')
        self.resizable(width=False, height=False)
        self.grid_columnconfigure(0, weight=1)

        # self._test()

    def select_mode(self):
        self.twl.set_mode(self.radVar.get())

    def select_dir(self):
        sel_dir = filedialog.askdirectory()

        if sel_dir:
            self.dir_selected = True
            root = Node(sel_dir)
            t = Tree(root)
            self.twl = TwL(t)
            self.select_mode()
            # self.twl._preOrder(self.twl.getTreeRoot())
            self.twl.set_items(self.twl.get_tree_root())
            print(self.twl.items)

            self.dir_text.delete('1.0', END)
            self.dir_text.insert(END, self.twl.get_tree_root_item())

    def change_img_name(self):
        if self.dir_selected:
            try:
                self.twl.clear_err_list()
                self.twl.change_file(self.twl.get_tree_root())
                self.state_text.configure(state='normal')
                self.state_text.delete('1.0', END)
                self.state_text.tag_configure("center", justify='center')
                self.state_text.insert(END, "Name Changed")
                self.state_text.tag_add("center", 1.0, "end")
                self.state_text.configure(state='disable')
                self.err_text.configure(state='normal')
                self.err_text.delete('1.0', END)

                for err_path in self.twl.err_list:
                    self.err_text.insert(END, err_path+'\n')
                self.err_text.configure(state='disable')
            # except NameError:
            #     msgbox.showerror("Error", "Select Folder")
            except Exception as err:
                msgbox.showerror("Error", err)
        else:
            msgbox.showerror("Error", "Select Directory")

    def select_date_file(self):
        sel_file = filedialog.askopenfile()

        if sel_file:
            self.file_selected = True
            file_name = sel_file.name
            df = pd.read_excel(file_name, sheet_name="Sheet1")

            self.twl.set_dates(df)

            self.file_text.delete('1.0', END)
            self.file_text.insert(END, file_name)

    def change_date(self):
        if self.file_selected:
            try:
                self.twl.clear_err_list()
                self.twl.change_exif(self.twl.get_tree_root())
                self.state_text.configure(state='normal')
                self.state_text.delete('1.0', END)
                self.state_text.tag_configure("center", justify='center')
                self.state_text.insert(END, "Date Changed")
                self.state_text.tag_add("center", 1.0, "end")
                self.state_text.configure(state='disable')
                self.err_text.configure(state='normal')
                self.err_text.delete('1.0', END)

                for err_path in self.twl.err_list:
                    self.err_text.insert(END, err_path+'\n')
                self.err_text.configure(state='disable')
            except Exception as err:
                msgbox.showerror("Error", err)
        else:
            msgbox.showerror("Error", "Select date file")

    def _test(self):
        self.err_text.configure(state="normal")
        self.err_text.delete('1.0', END)
        for i in range(20):
            self.err_text.insert(END, str(i)*10 + "\n")