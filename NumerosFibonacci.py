"""
_maxnumber = 5
def fibonacci(_maxnumber):
    pass

hola=fibonacci(_maxnumber)"""

def fibonacci(maxnumber):
    l = []
    suma = 0
    num = 1
    if(maxnumber > 0):
        for _ in range(maxnumber):
            l.append(suma)
            suma, num = num, suma+num
    return l

print(fibonacci(1))
print(fibonacci(3))
print(fibonacci(11))
print(fibonacci(12))