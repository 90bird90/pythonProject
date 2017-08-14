#! encoding=utf-8

import xlrd
import xml.dom.minidom
import os


def open_excel(file):
	try:

		#引入xlrd包，调用他的open_workbook方法打开excel文件读取里面的数据，这个方法参数很多，主要是第一个，传入要解析的excel文件。
		data = xlrd.open_workbook(file)
		return data
	except Exception, e:
		print str(e)


def translate_excel_to_xml(excel_absolute_path, name, generate_xml_dir, colnnameindex=0, by_index=0):
	# 解析excel文件
	data = open_excel(excel_absolute_path)

	# 获取需要的工作表
	'''
	table = data.sheets()[index] index就是就是左下角的工作表的索引顺序，从0开始。
	table = data.sheets()[index] index就是就是左下角的工作表的索引顺序，从0开始。
	table = data.sheet_by_index(index) 看下他们的实现发现这个和上面的其实一样的，只是上一种是data.sheets()或获取此excel中的所有表，生成一个list，再通过列表的下标取到我们需要的表。
	table = data.sheet_by_name(u'sheet_name')，这个是通过表的名称来获取的

	'''
	table = data.sheets()[by_index]

	# 行数
	nrows = table.nrows
	# 列数
	ncols = table.ncols

	# 创建dom文档对象
	doc = xml.dom.minidom.Document()

	# 创建根元素
	info = doc.createElement('info')

	# 将根元素添加到文档中区
	doc.appendChild(info)

	file_name = name.strip().split('.')[0]


	#这样可以获取到整行的数据 talbe.row_values(index) ，index就是要获取的所在行数，返回的是一个list列表保存数据。
	# 通用的道理，table.col_values(index)，就是index列的数据。返回list。

	'''
	.获取单元格的数据。
	通过table.cell(row_index, col_index)可以得到excel中row_index行col_index列的数据，
	这样得到的其实是这样的数据：类型: 字段名（unicode编码），我们这里使用的是utf-8编码，
	比如我们这个excel表中的第一行第一列的table.cell(0, 0)得到的就是：text:u'itemID'。
	要是获取值就使用table.cell(row_index, col_index).value即可。
	
	'''
	for nrow in range(3, nrows):
		# 创建元素
		item = doc.createElement(file_name.encode('utf-8'))
		for ncol in range(0, ncols):
			# colnames = table.col_values(ncol)
			# print colnames
			# print table.cell(nrow, ncol).value

			key = "%s" % table.cell(1, ncol).value

			if len(key) > 0:

				value = table.cell(nrow, ncol).value
				if isinstance(value, float):
					value = '%0d' % value

				# print type(key), type(value)
				# 将数据都作为xml中元素的属性，属性名就是第一行的值，属性值就是某一行某一列的值
				item.setAttribute(key.encode('utf-8'), value.encode('utf-8'))
		# print table.cell(0, ncol).value
		# 将此元素作为根元素的子节点

		info.appendChild(item)

	# 要生成的xml文件名
	generate_xml_name =	file_name + '.xml'
	# 要生成的xml文件到某个目录的绝对路径
	geneate_xml_dir = os.path.join(generate_xml_dir, generate_xml_name)

	f = open(geneate_xml_dir, 'w')

	context = doc.toprettyxml()
	#doc.writexml(f)
	f.write(context)  # 可以使生成xml有好看的格式，要是不需要，可以使用上一行的代码
	f.close()


def find_assign_xlsx(xlsx_path, generate_xml_dir):
	for name in os.listdir(xlsx_path):
		if name.endswith('.xlsx'):
			# 生成excel文件的绝对路径
			excel_absolute_path = os.path.join(xlsx_path, name)
			# 解析excel并转成xml
			translate_excel_to_xml(excel_absolute_path, name, generate_xml_dir)


if __name__ == "__main__":
	excel_src_path = r'E:\beiyan\ProjectX\res\TableTool\common_configs'
	generate_xml_dir = r'E:\data'

	find_assign_xlsx(excel_src_path.decode('utf-8'), generate_xml_dir)