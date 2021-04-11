base = int(input("Ingrese un numero"))
expo = int(input("Ingrese expo"))

po = 1
c = 1

while c <= po:
    po = po * base
    c = c + 1

print(base, "elevado a ", expo, ": ", po)
