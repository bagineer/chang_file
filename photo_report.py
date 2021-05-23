'''
# import tkinter as tk
#
# ##############################
# # 1. GUI Programming
# ##############################
#
# # Create a window
# window = tk.Tk()
# window.geometry("600x400")
# window.resizable(width = False, height = False)
# window.title("Shinil")
#
# window.withdraw()
# folder_selected =
#
# window.mainloop()
# #

from tkinter import filedialog
from tkinter import *
import os
import myLib

root = Tk()
root.withdraw()
selDir = filedialog.askdirectory()

s = myLib.Stack()   # Create a stack
s.push(selDir)

rs = myLib.Stack()  # reverse stack

while not s.isEmpty():
    curDir = s.pop()
    curNode = myLib.Node(curDir)

    dirList = os.listdir(curDir)

    # flag = 0
    for _dir in dirList:
        subDir = curDir + '/' + _dir
        if os.path.isdir(subDir):
            rs.push(subDir)
            # flag = 1

    print("================")
    while not rs.isEmpty():    # push items into stack in reverse order
        s.push(rs.pop())


# if flag == 0:
#     print("End of directory")
# else:
#     print("More directories")

s.print()
'''


'''
from tkinter import filedialog
from tkinter import *
import tkinter.messagebox as msgbox
import tkinter.font as tkFont
import myLib

def selectDir():
    selDir = filedialog.askdirectory()

    if selDir:
        root = myLib.Node(selDir)
        global twl
        t = myLib.Tree(root)
        twl = myLib.TwL(t)
        t._preOrder(root)

        dirText.delete('1.0', END)
        dirText.insert(END, twl.tree.root.item)

def changeImgName():
    try:
        twl.clearErrList()
        twl.changeFile(twl.tree.root)
        stateText.configure(state = 'normal')
        stateText.delete('1.0', END)
        stateText.insert(END, 'succeed')
        stateText.configure(state = 'disable')
        errText.configure(state='normal')
        errText.delete('1.0', END)
        for errPath in twl.errList:
            errText.insert(END, errPath+'\n')
        errText.configure(state='disable')
    except NameError:
        msgbox.showerror("Error", "Select Folder")
    except Exception as err:
        msgbox.showerror("Error", err)


window = Tk()
window.geometry('{}x{}'.format(400, 300))
window.title('Shinil_Nowon')
window.config(bg = 'powderblue')
window.resizable(width = False, height = False)
window.grid_columnconfigure(0, weight = 1)

font = tkFont.Font(size = 10, weight = 'bold')

frame1 = Frame(window, bg = 'powderblue')
frame1.grid(row = 0, column = 0, padx = 5, pady = 10, sticky = 'EW')
frame1.grid_columnconfigure(1, weight = 1)
frame2 = Frame(window, bg = 'powderblue')
frame2.grid(row = 1, column = 0, padx = 5, pady = 10, sticky = 'EW')
frame2.grid_columnconfigure(0, weight = 1)
frame3 = Frame(frame2, bg = 'powderblue')
frame3.grid(row = 1, column = 0, sticky = 'NESW')
frame3.grid_columnconfigure(0, weight = 1)

selBtn = Button(frame1, text = 'Select Folder', command = selectDir, bg = 'white')
selBtn.grid(row = 0, column = 0, sticky = 'EW')

dirText = Text(frame1, height = 1)
dirText.grid(row = 0, column = 1, padx = 5, sticky = 'EW')

changeBtn = Button(frame1, text = 'Change Image Name', command = changeImgName, bg = 'white')
changeBtn.grid(row = 1, column = 0, sticky = 'EW')

stateText = Text(frame1, height = 1)
stateText.grid(row = 1, column = 1, padx = 5, stick = 'EW')

errLabel = Label(frame2, height = 1, text='directories with error', bg = 'powderblue', font = font)
errLabel.grid(row = 0, column = 0)

errText = Text(frame3, height = 10)
errText.grid(row = 0, column = 0)
s = Scrollbar(frame3)
s.grid(row = 0, column = 1, sticky = 'NS')
s.config(command = errText.yview)



window.mainloop()
'''

import myLib

app = myLib.App(None)
app.mainloop()