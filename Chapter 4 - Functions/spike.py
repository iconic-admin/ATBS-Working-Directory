import time, sys

try:
    while True: #the main loop of the program
        #draw lines of increasing length:
        for i in range(1, 9):
            print('-' * (i * i))
            time.sleep(0.1)

        #draw with decreasing length:
        for i in range(7, 1, -1):
            print('-' * (i * i))
            time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()