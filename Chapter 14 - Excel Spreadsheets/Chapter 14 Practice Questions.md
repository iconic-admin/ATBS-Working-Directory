1. openpyxl.load_workbook() returns a value of the workbook datatype. The workbook object represents an excel file sort of like how a file objectt represents an opened text file.
2. wb.sheetnames contains the names of existing sheets in a workbook object. A newly opened workbook will contain one sheet named 'Sheet'.
3. To retrieve the worksheet object for a sheet named 'Sheet1' you could assign the sheet object to a variable like sheet = wb['Sheet1']. You could then use this variable to manipulate the sheet object. sheet.title, type(sheet), etc.
4. To retrieve the worksheet object for the workbook's active sheet: wb.active returns the workbook's active sheet, this could be assigned to a varaiable.
5. Assuming a sheet object is assigned to the varaiable 'sheet'; sheet['C5'] will return the value stored in C5 of that sheet.
6. To change the value stored in C5; sheet['C5'] = <input goes here>
7. To retrieve a cell's row an column as integers; column_index_from_string(), for example column_index_from_string('AA') would return 27. Rows are already stored as numbers. Also, if cell = sheet['C5'], cell.row and cell.column will return the numerical values of the cell's row and column.
8. sheet.max_row and sheet.max_column return the maximum existing number of rows and columns in a sheet and their data type is integer.
9. To get the numerical index for a column; column_index_from_string('M')
10. To get the string name for row 14 you would call; assuming the cell variable has already been assigned, cell.get_column_letter(14) would return 'M' with is the 14th column.
11. To retrieve a tuple of the cell objects from A1 to F1; sheet['A1':'F1'] returns a tuple of these cell objects.
12. Assuming wb = <a workbook object>; wb.save('example3_copy.xlsx') would save the object as the example file name.
13. To set a formula in a cell; set the value of the cell equal toa string of the formula, i.e. sheet['D5'] = <formula goes here>. Note, the formula will not execute until Excel opens the file.
14. to retrieve the result of a formula for a cell rather than the formula itself; sheet['D5'].value. sheet['D5'] would return the formula.
15. To set the height of row 5 to 100; sheet.row_dimensions[5].height = 100
16. To hide column C; column_dimensions['C'].hedden = True
17. A freeze pane is stuck to the visible window, like a heading. Scrolling around the sheet, the freezed pane will remain in view.
18. The five functions to call to create a bar chart; 
    - chart.Reference()
    - chart.Series()
    - chart.BarCHart()
    - chartObj.append(seriesObj)
    - add_chart()