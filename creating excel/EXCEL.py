import xlsxwriter

data9 = xlsxwriter.Workbook("data9.xlsx")

worksheet = data9.add_worksheet("data9.xlsx")


row = 0
column = 0
content = ["sassy","siayn","ben","jonny","sparta"]
for item in content:
    worksheet.write(row,column,item)
    row += 1

worksheet.name = "Data 9 Team"

data9.close()# alywas last line

print(row)
print(column)
print(content)
