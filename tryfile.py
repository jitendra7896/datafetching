import pandas as pd
def add_status(df3,df2):
    status = pd.Series([])
    for i in range(len(df2)):
        if df3.iloc[:, 0][i] == "disable" or pd.isna(df3.iloc[:, 0][i]) == True:
            status[i] = 0
        else:
            status[i] = 1
    x = len(df2.columns)
    df2.insert(x, "Status", status)
def vendor_code(df3,df2):
    new_vendor_code=pd.Series([])
    for i in range(len(df2)):
        if pd.isna(df3.iloc[:,2][i])==True:
            new_vendor_code[i]=df3.iloc[:,1][i]
        else:
            new_vendor_code[i]=df3.iloc[:,2][i]

    x = len(df2.columns)
    df2.insert(x, "New Vendor Code", new_vendor_code)
def newprice(df3,df2):
    new_price=pd.Series([])
    for i in range(len(df2)):
        if pd.isna(df3.iloc[:,4][i]) == True:
            new_price[i] = df3.iloc[:,3][i]
        elif int(df3.iloc[:,4][i])>int(df3.iloc[:,3][i]):
            new_price[i] = df3.iloc[:,4][i]
        else:
            x = int(df3.iloc[:,4][i])
            y = int(df3.iloc[:,3][i])
            try:                        #(AE-AD)/AD% <80%
                a=0
                if(x-y)/y*100>80:
                    new_price[i] = df3.iloc[:, 4][i]
                else:
                    q=1/a
            except ZeroDivisionError:
                new_price[i] = df3.iloc[:, 3][i]
                print("ValueError:value looks wrong old value is placed")
    x = len(df2.columns)
    df2.insert(x, "New Price", new_price)
