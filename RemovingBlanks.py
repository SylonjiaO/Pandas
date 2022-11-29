import pandas as pd #alias 

try:
    df1 = pd.read_excel('C:/YU Learn to Code/Pandas/RaviList.xlsx')
    print(df1)
    df=df1.dropna()#will remove blank rows
    print(df)
    print(df.duplicated())#finds duplicate data
    df2=df.drop_duplicates()#drops duplicate values
    print(df2)
    writer=pd.ExcelWriter("C:/YU Learn to Code/Pandas/Sylonjia2.xlsx") #To Create a New File
    df2.to_excel(writer)
    writer.save() #perma save the data
    print('Data Saved')
    print('Total Number of rows = %d' %df2['Name'].count())
    print('List Of organization names: ', set(df2['Organization']) )
except FileNotFoundError:
    print("Sorry, NO File at This Location")
except Exception as k:
    print("Sorry, Something Went Wrong" +k)
finally:
    print("The End")
