from math import sqrt, tan, pi
import xlrd

def predict(values = None):
    
    
    
    workbook = xlrd.open_workbook('C:\Users\Angus\Desktop\stardata.xlsx')
    sheet = workbook.sheet_by_index(0)
    sheet.cell_value(0, 0)
    result = 'not found'
    for i in range(sheet.nrows):
        if (sheet.cell_value(i, 0) == values['body']):
            result = sheet.cell_value(i, 1).encode('utf-8') + sheet.cell_value(i, 2).encode('utf-8') + str(sheet.cell_value(i, 3)) + str(sheet.cell_value(i, 4).encode('utf-8'))
    
    return result