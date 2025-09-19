# this script take three arguments, a row number (N)
# a number of blank rows (M), and a file name. At row 
# N, this script inserts M number of new blank rows.

import openpyxl, sys

N = int(sys.argv[1])
M = int(sys.argv[2])
fileName = sys.argv[3]

wb = openpyxl.load_workbook(fileName)
sheet = wb.active

# for i in range(M):
    # sheet.insert_rows(N)

sheet.insert_rows(N, M)

wb.save(fileName)