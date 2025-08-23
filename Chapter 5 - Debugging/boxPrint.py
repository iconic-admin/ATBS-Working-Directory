def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

try:
    boxPrint('*', 4, 4)
    boxPrint('0', 20, 5)
    boxPrint('x', 1, 3)
    boxPrint('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))
try:
    boxPrint('ZZ', 3, 3)
except Exception as err:
    print('An exception has happened: ' + str(err))