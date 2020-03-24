import xlsxwriter

data9 = xlsxwriter.Workbook("data9.xlsx")

worksheet = data9.add_worksheet("data9.xlsx")

worksheet.write("A1","data9")


worksheet.write("A2", "Sassy")
data9.close()# alywas last line 
