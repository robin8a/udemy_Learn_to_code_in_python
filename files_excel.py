import pandas as pd

excel_file = pd.ExcelFile("/Users/robin8a/Desktop/sales.xlsx")
print(excel_file.sheet_names)

sheet = excel_file.parse('sales')

print("---------")
print('sheet: ', sheet)
print("---------")
print('sheet type: ', type(sheet))
print("---------")
print('sheet Amount: ', sheet.Amount.sum())
print("---------")
print('sheet Row: \n', sheet.loc[0])
print('sheet Row: \n', sheet.loc[0, "Amount"])
print("---------")
sheet.set_index("Customer", inplace = True)
print(sheet.loc["MMC Inc."])
print("---------")