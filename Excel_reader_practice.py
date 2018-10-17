# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 13:45:04 2018

@author: Michael
"""
import xlrd

#importing an excel file and grabbing a specific worksheet
workbook = xlrd.open_workbook('C:\Users\Michael\Documents\Practice.xlsx')
worksheet = workbook.sheet_by_index(0)

#workbook and worksheet attributes
print "The number of worksheets is", workbook.nsheets
print "Worksheet name:", worksheet.name, '\n' "Number of rows:", worksheet.nrows, '\n' "Number of columns:", worksheet.ncols

#select cell values
print worksheet.cell(0,0).value
print "Cell F19 is:", worksheet.cell_value(rowx = 19, colx = 5)

#looping over a select row in this case to find column headers
i = 0
for worksheet.cell(0, i).value in worksheet.row(1):
    if worksheet.cell(0, i).value != xlrd.empty_cell.value:
      print worksheet.cell(0, i).value
      i = i + 1
    else:
      break
  
#printing each row for n rows from the worksheet
for j in range(worksheet.nrows):
    print worksheet.row(j)
    