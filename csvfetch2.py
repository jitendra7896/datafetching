import tkinter as tk           #pip install tk
from tkinter import filedialog
from datetime import datetime  #pip install datetime
import pandas as pd            #pip install pandas
root = tk.Tk()                  #creating base root tk object

canv = tk.Canvas(root, width=500, height=300, bg='lightgreen')         #creating a window
canv.pack()
import_file_path=pd.ExcelFile("Stock_Report.xlsx",)
sheet_name=tk.StringVar(root,value='Online Catalog')
filesname=tk.StringVar()


'''function to import excel file
if the extension is not xlsx or csv the file will not open'''

def getExcel():
    global data
    global import_file_path
    import_file_path = filedialog.askopenfilename()
    try:
        import_file_path.endswith('xlsx' or 'csv')
        data = pd.ExcelFile(import_file_path)
        w = tk.Label(root, text="            file selected  ",bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))
        canv.create_window(430, 30, window=w)

    except:
        print("NameError : File_Type_Not_Correct")
        root.destroy()

'''function to print the sheet if sheet name incorrect window will be closed
if correct it will print starting 10 lines of sheet'''

def submit():
    global df
    try:
        df = pd.read_excel(import_file_path,sheet_name.get(),usecols=[1,4,6])
        c = tk.Label(root, text=" data selected", bg='lightgreen', fg='black',
                     font=('helvetica', 10, 'bold'))
        canv.create_window(450, 70, window=c)
    except:
        print("Find_Error : Sheet_You_Searched_For_Not_Present")
        root.destroy()

'''create a file and write data into it'''
def crtfile():
    try:
        q="Stock_Report_"
        dateTimeObj = datetime.now()
        timeStr = dateTimeObj.strftime("%H%M%S%f")
        tstr=q+timeStr+".xlsx"
        df.to_excel(tstr,index=False)
    except:
        print("file name is wrong or data not selected")
    finally:
        root.destroy()

'''buttons and inputs'''

browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='black',
                               font=('helvetica', 12, 'bold'))                                          #importing file
canv.create_window(250,30, window=browseButton_Excel)
w = tk.Label(root,text='Default=Stock Report', bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))                                               #label sheet name
canv.create_window(430, 30, window=w)



browseButton_Excel3 = tk.Label(root,text='Sheet Name', bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))                                               #label sheet name
canv.create_window(70, 70, window=browseButton_Excel3)


browseButton_Excel2 = tk.Entry(textvariable=sheet_name, bg='white', fg='black',
                               font=('helvetica', 12, 'bold'))                                               #entry button
canv.create_window(220, 70, window=browseButton_Excel2)


sub_btn=tk.Button(root,text = 'Submit',command=submit,bg='green',fg='black')
canv.create_window(370, 70, window=sub_btn) #submit button

crflabel = tk.Label(root,text='Enter name of new file to copy the output data', bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))                                               #label sheet name
canv.create_window(180, 110, window=crflabel)
crt_btn=tk.Button(root,text = 'Create File',command=crtfile,bg='green',fg='black')
canv.create_window(380, 110, window=crt_btn)                                                               #submit button


root.mainloop()
