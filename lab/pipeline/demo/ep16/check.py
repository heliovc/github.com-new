from openpyxl import load_workbook

wb = load_workbook("report.xlsx")
print(wb.sheetnames)
ws = wb["By city"]
for row in ws.iter_rows(values_only=True):
    print(row)
