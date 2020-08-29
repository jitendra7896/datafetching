import tkinter as tk           #pip install tk
from tkinter import filedialog
import pandas as pd            #pip install pandas
import tryfile
root = tk.Tk()                  #creating base root tk object

canv = tk.Canvas(root, width=500, height=300, bg='lightgreen')         #creating a window
canv.pack()

sheet_name=tk.StringVar()
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
        w = tk.Label(root, text="file selected",bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))
        canv.create_window(450, 30, window=w)
    except:
        print("file type not correct")
        root.destroy()

'''function to print the sheet if sheet name incorrect window will be closed
if correct it will print starting 10 lines of sheet'''

def submit():
    global df
    try:
        df = pd.read_excel(import_file_path,sheet_name.get(),usecols=[1,4,6])    #reading specific column of file
        tryfile.master(df)                                                      #using tryfile module user created
    except:
        print("Sheet name din't match")
        root.destroy()

'''create a file and write data into it'''
def crtfile():
    try:
        df.to_excel(filesname.get())
        print(filesname.get())
    except:
        print("file name is wrong or data not selected")
        root.destroy()

        '''buttons and inputs'''

browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white',
                               font=('helvetica', 12, 'bold'))                                          #importing file
canv.create_window(250,30, window=browseButton_Excel)


browseButton_Excel3 = tk.Label(root,text='Sheet Name', bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))                                               #label sheet name
canv.create_window(100, 70, window=browseButton_Excel3)


browseButton_Excel2 = tk.Entry(textvariable=sheet_name, bg='white', fg='black',
                               font=('helvetica', 12, 'bold'))                                               #entry button
canv.create_window(250, 100, window=browseButton_Excel2)


sub_btn=tk.Button(root,text = 'Submit',command=submit,bg='green',fg='white')
canv.create_window(400, 100, window=sub_btn) #submit button

crflabel = tk.Label(root,text='Enter name of new file to copy the output data', bg='lightgreen', fg='black',
                               font=('helvetica', 10, 'bold'))                                               #label sheet name
canv.create_window(210, 140, window=crflabel)

crfl = tk.Entry(textvariable=filesname, bg='white', fg='black',
                font=('helvetica', 12, 'bold'))  # entry button
canv.create_window(250, 170, window=crfl)

crt_btn=tk.Button(root,text = 'Create File',command=crtfile,bg='green',fg='white')
canv.create_window(400, 170, window=crt_btn)                                                               #submit button


root.mainloop()
