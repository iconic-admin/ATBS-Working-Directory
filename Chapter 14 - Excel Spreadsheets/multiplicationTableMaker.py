# this script takes a number N in the command line
# and creates an Excel spreadsheet containing a
# multiplication table up to N x N.
# Row and column 1 should have labels and be in bold

import openpyxl, sys
from openpyxl.styles import Font

N = int(sys.argv[1])
boldFont = Font(bold = True)

workBook = openpyxl.Workbook()
# default sheetname is 'Sheet'
sheet = workBook['Sheet']

for row in sheet.iter_rows(min_row=1, max_row=N+1, min_col=1, max_col=N+1):
    for cell in row:
        if cell.row == 1 and cell.column == 1:
            cell.value = ''
        elif cell.row == 1:
            cell.value = cell.column - 1
            cell.font = boldFont
        elif cell.column == 1:
            cell.value = cell.row - 1
            cell.font = boldFont
        else:
            cell.value = (cell.row - 1) * (cell.column - 1)

workBook.save('multiplicationTableOutput.xlsx')