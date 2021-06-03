import openpyxl
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.styles import Font

#opening excel document

wb  = openpyxl.load_workbook("F:\\Test.xlsx")
# print(type(wb))

#getting sheet from workbook
print(wb.sheetnames)

# sheet=wb['text']
sheet = wb.active
# print(sheet.title)

ansheet = wb.active
print(ansheet.title)

#Getting cell value from sheet
cell_value =sheet['A1'].value
print(cell_value)

#get cell and then value
cell = sheet['A1']
print(cell.value)

#get row, column and value from cell
print('Row %s, Column %s is %s' %(cell.row, cell.column,cell.value))

print('cell %s is %s' %(cell.coordinate, cell.value))

print(sheet.max_row)
print(sheet.max_column)

#Converting between column letters and Numbers
print(get_column_letter(109))
print(get_column_letter(sheet.max_column))
print(column_index_from_string("DE"))

#Getting Rows and Columns from the Sheets

print(tuple(sheet['A1':'D3']))
for rowOfCellObjects in sheet['A1':'D1']:
    for cellobject in rowOfCellObjects:
            # print(cellobject.coordinate, cellobject.value)
            print(cellobject.value)

####Writing to Excel
print('\n\n-----Writing to Excel------\n\n')
print(sheet.title)
sheet.title = 'TextChanged'
wb.save('F:\\Test.xlsx')    # this saves workbook with new sheet name

#Create new file
print("----Creating New Excel file -----")

new_wb = openpyxl.Workbook()    #this step creats a empty excel object
# new_wb.save("F:\\newpython.xlsx")   #this step will create file on disk

#Createing and Removing sheet
print(new_wb.sheetnames)
new_wb.create_sheet()

print(new_wb.sheetnames)

#Del sheet
del new_wb['Sheet']

#Writing values to Cell
sh = new_wb.active
sh['A1'] = 'Count below'
# Mergind and Unmerging Cells


for i in range(1,1001):
    cellno = 'A'+str(i)

#Font object attributes - name - name of font like Arial etc,size - like 10,16 etc,bold =True/False,italic=True/False,

    newFont=Font(name='Bodoni MT Black',size=16,italic=False)
    if(i%2==0):
        cellno = 'B'+str(i)
        newFont=Font(name='Calibri',size=26,italic =True)
    # print(cellno)

#Formulas e.g. SUM
    if (i==500):
        sh['C500']='=SUM(A1:B499)'

#Setting Row height and Column Width
    sh.row_dimensions[1].height =70
    sh.column_dimensions['B'].width=20
    # sh.column_dimensions['B'].height=30

    sh[cellno].font = newFont
    sh[cellno] = i

#Merge Cells

sh.merge_cells('C1:C5')   #overrides cell values

#Freezing Panes
# sh.freeze_panes = 'A2' #Row1 Freezes
# sh.freeze_panes = 'B1' #Column A freezes
# sh.freeze_panes = 'C1' #Columns A and B freeze
sh.freeze_panes = 'C2' # Row 1 and Column A& B Freeze
# sh.freeze_panes = 'A1' # no frozen panes
# sh.freeze_panes = None # no frozen panes

new_wb.save("F:\\newpython.xlsx")  # save all the changes, also overrides files if already present


####openpyxl supports charts as well


