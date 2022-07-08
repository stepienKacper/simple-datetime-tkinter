#           modules
import datetime as dt
from time import strftime
from tkinter import *

#           app
root = Tk()
root.title('My first app')
root.geometry('400x157')
root.resizable(0, 0)
root.iconbitmap('clock.ico')

date1 = dt.datetime.now()
date2 = dt.datetime.now()

#           Labels
Label1 = Label(root, text=f'{date1:%A %B %d %Y}', font="Calibri, 20")
Label2 = Label(root, text=f'{date2: %H:%M:%S}', font="Calibri, 40")
Label3 = Label(root, text='Copyrighted by Kacper Stępień', font='Calibri, 8', fg='white', bg='red')


#           Functionality
def current_time():
    time_string = strftime("%H:%M:%S")
    Label2.config(text=f'{time_string}')
    root.after(1000, current_time)

    return current_time


if __name__ == '__main__':
    current_time()
    Label2.pack()
    Label1.pack()
    Label3.place(x=0, y=138)

    root.mainloop()
