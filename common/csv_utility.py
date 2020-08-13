
import csv,sys

filename = '搜索结果.csv'
data = []
try:
	with open(filename) as f:
		reader = csv.reader(f)
		header = next(reader)
		data = [row for row in reader]
except csv.Error as e:
	print("Error reading csv file at line %s: %s" % (reader.line_num, e))
	sys.exit(-1)

if header:
	print (header)
	print('===========================')
for datarow in data:
	#打印 ID和 bug 标题
	print ('%s %s' % (datarow[0],datarow[1]))
