import xlrd
# 1.获取工作表对象
book=xlrd.open_workbook('TestExcel.xlsx')
print('表单的数量:',book.nsheets)#获取工作表的表单数量
print('表单的名称:',book.sheet_names())#获取工作表中的表单名称

#2.获取某个表单对象
sheet1=book.sheet_by_index(0)#通过索引获取表单对象
# sheet1=book.sheet_by_name('2017')#通过名字获取表单对象

#3.获取表单信息
print('表单名',sheet1.name)
print('表单索引',sheet1.number)
print('表单行数',sheet1.nrows)
print('表单列数',sheet1.ncols)
#4.单元格操作
print("单元格内容",sheet1.cell_value(rowx=0,colx=0))#获取指定单元格内容(行，列索引)
print("第一行内容",sheet1.row_values(0))#获取指定行内容
print("第一列内容",sheet1.col_values(0))#获取指定列内容