import tkinter as tk           #pip install tk
from tkinter import filedialog
import pandas as pd            #pip install pandas

root = tk.Tk()                  #creating base root

canv = tk.Canvas(root, width=300, height=300, bg='lightgreen')         #creating a window
canv.pack()

sheet_name=tk.StringVar()

'''function to import excel file
if the extension is not xlsx or csv the file will not open'''

def getExcel():
    global data
    import_file_path = filedialog.askopenfilename()
    try:
        import_file_path.endswith('xlsx' or 'csv')
        data = pd.ExcelFile(import_file_path)
    except:
        print("file type not correct")
        root.destroy()

'''function to print the sheet if sheet name incorrect window will be closed
if correct it will print starting 10 lines of sheet'''

def submit():
    global df
    try:
        df = data.parse(sheet_name.get())
        print (df.head(10))
    except:
        print("No Sheet name match")
        root.destroy()

'''buttons and inputs'''

browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))                                          #importing file
canv.create_window(150, 150, window=browseButton_Excel)


browseButton_Excel3 = tk.Label(root,text='Sheet Name', bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))                                               #label sheet name
canv.create_window(50, 180, window=browseButton_Excel3)


browseButton_Excel2 = tk.Entry(textvariable=sheet_name, bg='white', fg='black',
                               font=('helvetica', 12, 'bold'))                                               #entry button
canv.create_window(150, 200, window=browseButton_Excel2)


sub_btn=tk.Button(root,text = 'Submit',command=submit,bg='green',fg='white')
canv.create_window(150, 250, window=sub_btn)                                                               #submit button


root.mainloop()