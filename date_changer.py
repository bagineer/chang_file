from tkinter import *
from tkinter import filedialog
from datetime import datetime


class App(Tk):
    def __init__(self, master):
        Tk.__init__(self, master)
        self.master = master
        self._initialize()
        pass

    def _initialize(self):
        # Frame
        frame1 = Frame(self)
        frame1.grid(row=0, column=0, padx=10, pady=10, sticky='EW')
        frame2 = Frame(self)
        frame2.grid(row=1, column=0, padx=10, pady=10, sticky='EW')
        frame2_1 = Frame(frame2)
        frame2_1.grid(row=1, column=0, padx=10, pady=10, sticky='EW')

        year_frame = Frame(frame2_1)
        year_frame.grid(row=0, column=0, padx=10, pady=10)
        month_frame = Frame(frame2_1)
        month_frame.grid(row=0, column=1, padx=10, pady=10)
        day_frame = Frame(frame2_1)
        day_frame.grid(row=0, column=2, padx=10, pady=10)

        sel_file_btn = Button(frame1, text="Select File")
        sel_file_btn.grid(row=0, column=0)
        sel_file_text = Text(frame1, height=1, width=30)
        sel_file_text.grid(row=0, column=1, padx=10)

        year_text = Text(year_frame, height=1, width=5)
        year_text.grid(row=0, column=0)
        month_text = Text(month_frame, height=1, width=3)
        month_text.grid(row=0, column=0)
        day_text = Text(day_frame, height=1, width=3)
        day_text.grid(row=0, column=0)

        year = Listbox(year_frame, height=10, width=5, selectmode="extended", exportselection=0)  # exportselection : select item in multiple listboxes
        year.grid(row=1, column=0)
        month = Listbox(month_frame, height=10, width=3, selectmode="extended", exportselection=0)
        month.grid(row=1, column=0)
        day = Listbox(day_frame, height=10, width=3, selectmode="extended", exportselection=0)
        day.grid(row=1, column=0)
        cur_date = datetime.today()

        yb_frame = Frame(year_frame, height=20, width=20)
        yb_frame.grid(row=0, column=1)
        yb_frame.grid_propagate(False)
        yb_frame.columnconfigure(0, weight=1)
        yb_frame.rowconfigure(0, weight=1)
        year_btn = Button(yb_frame, height=5, width=5)
        year_btn.grid(row=0, column=0)

        mb_frame = Frame(month_frame, height=20, width=20)
        mb_frame.grid(row=0, column=1)
        mb_frame.grid_propagate(False)
        mb_frame.columnconfigure(0, weight=1)
        mb_frame.rowconfigure(0, weight=1)
        month_btn = Button(mb_frame, height=5, width=5)
        month_btn.grid(row=0, column=0)

        db_frame = Frame(day_frame, height=20, width=20)
        db_frame.grid(row=0, column=1)
        db_frame.grid_propagate(False)
        db_frame.columnconfigure(0, weight=1)
        db_frame.rowconfigure(0, weight=1)
        day_btn = Button(db_frame, height=5, width=5)
        day_btn.grid(row=0, column=0)

        cur_year = cur_date.year
        cur_month = cur_date.month
        cur_day = cur_date.day
        ch, cm, cs = cur_date.hour, cur_date.minute, cur_date.second
        print(cur_year, cur_month, cur_day, ch, cm, cs)

        yy, mm, dd = 1980, 1, 1
        for i in range(70):
            if i < 12:
                month.insert(END, mm+i)
            if i < 31:
                day.insert(END, dd+i)
            year.insert(END, yy+i)


        year.select_set(cur_year-yy)    # select default value
        year.see(cur_year-yy)   # move to default value
        month.select_set(cur_month-mm)
        month.see(cur_month-mm)
        day.select_set(cur_day-dd)
        day.see(cur_day-dd)


    def _make_calendar(self):
        pass

if __name__ == "__main__":
    app = App(None)
    app.mainloop()
