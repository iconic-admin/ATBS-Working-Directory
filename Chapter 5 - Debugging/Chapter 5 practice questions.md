Practice Questions
1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
    assert int(spam) < 10
2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are diﬀerent. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)
    assert lower(eggs) == lower(bacon)
    >>> assert 'hEllo'.lower() == 'hello'.lower()
    >>> assert 'hEllo'.lower() == 'hellao'.lower()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AssertionError
3. Write an assert statement that always triggers an
AssertionError.
    assert 1 ==2
4. What two lines must your program have to be able to call
logging.debug()?
    import logging
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
5. What two lines must your program have to make
logging.debug() send a logging message to a ﬁle named
programLog.txt?
    inport logging
    logging.basicConfig(filename='filenamehere.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
6. What are the ﬁve logging levels?
    debug
    info
    warning
    error
    critical
7. What line of code can you add to disable all logging messages in your program?
    logging.disable(logging.CRITICAL)
8. Why is using logging messages better than using print() to
display the same message?
    logging can easilly be disabled with one line, were prints statments would need to be romoved one at a time.
9. What are the diﬀerences between the Step Over, Step In, and
Step Out buttons in the debugger?
    Step Over - skips to the return of a function call
    Step In - goes to the next step in the program
    Step Out - goes to the end of a function if the debugger is in the middle of running one
10. After you click Continue, when will the debugger stop?
    Continue will cause the program to operate normally until it finishes running or reaches a break point.
11. What is a breakpoint?
    A developer set line were a debugger using the continue command will stop.
12. How do you set a breakpoint on a line of code in Mu?
    By clicking on the line number were you want the breakpoint to be