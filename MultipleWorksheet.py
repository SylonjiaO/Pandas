# How To Read Data From Excel File From Two Different Worksheets

import pandas as pd
df=pd.read_excel("C:/YU Learn to Code/Pandas/Recruitment.xlsx",sheet_name='Sheet1')
df1=pd.read_excel("C:/YU Learn to Code/Pandas/Recruitment.xlsx",sheet_name='Sheet2')
print("Recruitment in Year 2020")
print(df)
print("Recruitment in Year 2021")
print(df1)
