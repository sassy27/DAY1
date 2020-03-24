import openpyxl #fetch data from the excel file using python
path = "data9.xlsx" #importing module
data9_object = openpyxl.load_workbook(path) # gives the location of our file
data9_object = data9_object.active #active


print(data9_object.max_row, data9_object.max_column) #tells max rows and columns

data_sheet = data9_object.title # gets title
print(data_sheet)

# name_sheet = data9_object = "class9"
# print(data9_object.title())

get_data = data9_object.cell(row=2, column=1)  # gets a value
print(get_data.value)

data9_object.cell(row=1,column=1).value = "changed"