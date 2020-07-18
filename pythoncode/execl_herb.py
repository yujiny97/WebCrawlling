import openpyxl
from pythoncode import webfunction_herb as w

##엑셀파일 경로
workbook = openpyxl.load_workbook('C:/Users/i5533/OneDrive/바탕 화면/바탕화면정리/빅데이터공모전/xlsx/herbtable.xlsx')
worksheet=workbook['Forest']#sheet이름

name_range=worksheet['C2':'C100'] #이름
list_var=[]

for row in name_range:
    for cell in row:
        name=cell.value
        print(name)
        w.getpicture(name,300)