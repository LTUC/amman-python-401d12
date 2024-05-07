def fibonaci(n):
    'this function takes a number and returns the fibonaci value of it'
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 1
    if n <= 1:
        return n
    else:
        return (fibonaci(n-2)+fibonaci(n-1))