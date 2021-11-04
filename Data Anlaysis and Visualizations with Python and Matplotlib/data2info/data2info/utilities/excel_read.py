import pandas

def readExcel(data, showSample):
    df=pandas.read_excel(data)
    
    if showSample == True:
        print(df.head()) #show first 5 rows only
        print (df.shape) # show (row,col) count
        print(df.columns) # show names of columns

    return df
