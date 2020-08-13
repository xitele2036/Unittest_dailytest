import xlrd
from pprint import pprint
file = 'DefectList-20140424.xlsx'

wb = xlrd.open_workbook(filename = file)
wss = wb.sheet_names()
print(wss)

#ws = wb.sheet_by_name("DefectList")

ws = wb.sheet_by_index(1)
print(ws.name,ws.nrows,ws.ncols)
dataset = []

for r in range(ws.nrows):
	col = []
	for c in range(ws.ncols):
		col.append(ws.cell(r,c).value)
	dataset.append(col)
pprint (dataset)