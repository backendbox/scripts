#!/usr/local/bin/python3
import pandas as pd

writer = pd.ExcelWriter('output.xlsx')
df1 = pd.DataFrame(data={'col1':[1,1], 'col2':[2,2]})
df1.to_excel(writer,'Sheet1')
writer.save()

excel_path = 'output.xlsx'
d = pd.read_excel(excel_path, sheet_name=None)
print(d['Sheet1'])
