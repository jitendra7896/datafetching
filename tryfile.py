import tkinter as tk           #pip install tk
from tkinter import filedialog
import pandas as pd            #pip install pandas
import xlsxwriter
def crtfile():
    print("a")
def master(df2):
    master = tk.Tk()
    canv = tk.Canvas(master, width=800, height=900, bg='lightgreen')  # creating a window
    canv.pack()
    opt = tk.Label(master, text=df2.head(30), bg='lightgreen', fg='black',
                                       font=('helvetica', 10, 'bold'))  # label sheet name
    canv.create_window(200, 330, window=opt)


    master.mainloop()


