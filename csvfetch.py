import openpyxl
import os
os.getcwd()
os.chdir(r"C:\Users\jitu\Desktop")
import pandas as pd
file = "Stock_Report.xlsx"
data = pd.ExcelFile(file)
print(data.sheet_names) #this returns the all the sheets in the excel file
df = data.parse('Online Catalog')
#print(df.info)
print(df.head(10))
ps = openpyxl.load_workbook('Stock_Report.xlsx')
sheet = ps['Online Catalog']
print(sheet.max_row)