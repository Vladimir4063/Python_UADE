
def Fibonacci(_maxnumber):
    x, y = 0, 1

    for number in range(_maxnumber):
        y, x = x, x + y
        print(y)

Fibonacci(10)