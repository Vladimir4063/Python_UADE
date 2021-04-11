#Bienvenidos! Esto es la practica del verano.

import random

MAX = int(input("Ingrese largo de lista: "))
lista = [0] * MAX

for i in range(0,len(lista)):
    lista[i] = random.randint(0,50)
    
class objetos:
    def __init__(self, plato, cuchara, tenedor, cuchillo):
        self.plato = plato
        self.cuchara = cuchara
        self.tenedor = tenedor
        self.cuchillo = cuchillo
    def __repr__(self):
        return "Cant. Platos={0}, Cucharas={1}, Tenedores={2}, Cuchillo={3}\n".format(self.plato, self.cuchara, self.tenedor, self.cuchillo)

pla = int(input("Platos:"))
cuc = int(input("Cucharas:"))
ten = int(input("Tenedores:"))
cuch = int(input("Cuchillos:"))
lista.append(objetos(pla,cuc,ten,cuch))

print(lista)