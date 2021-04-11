#Repaso integrador, hecho en casa.
import random
"""
lar = int(input("Largo: "))
vector= [0] * lar
def numMayor(lar,vector):
    aux = 0
    for i in range(0,len(vector)):
        vector[i]=random.randint(0,50)
    for i in range(0,len(vector)):
        if vector[i] % 2 == 0 and vector[i] > aux:
            aux = vector[i]
    print(aux)
            

llama=numMayor(lar,vector)
print(vector)
"""
"""
#Ejercicio2#######################

f = int(input("Cant. : "))
matriz = [[0] * 5 for i in range(0,f)]
for fila in range(0,f): # fila entra primero.
    for colum in range(0,5): # colum luego.
        matriz[fila][colum]=random.randint(0,50)
for fila in range(0,f):
    for colum in range(0,5):
        print(matriz[fila][colum], end= " ")
    print()
nro = int(input("Nro: "))        
def Matriz(f,matriz,nro):
    fil = ""
    col = ""
    for fila in range(0,f):
        for colum in range(0,5):
            if matriz[fila][colum] == nro:
                fil = fila
                col = colum
                print("Fila: ", fil, "Columna: ",col)
    if fil == "" and col == "":
        return -1
llama=Matriz(f,matriz,nro)
if llama == -1:
    print("-1")
"""
#Ejercicio 3 #########################
"""
largo = int(input("Largo: "))
nombres = [""] * largo
for i in range(0,largo):
    nombres[i]="Nombre" + str(i)
nombreABuscar = input("Nombre a Buscar: ")
def BuscarNombre(largo, nombres, nombreABuscar):
    for i in range(0,largo):
        if nombres[i] == nombreABuscar:
            nom = i
            print("Posicion: ", nom)
llamador = BuscarNombre(largo, nombres, nombreABuscar)
"""
#Ejercicio 4 ##########################
class peliculas:
    def __init__(self, nombre, año, genero):
        self.nombre = nombre
        self.nombre = año
        self.genero = genero
    def __repr__(self):
        return "{0}, {1}, {2}".format(self.nombre, self.año, self.genero)
    
largo = int(input("Largo: "))
lstPeliculas1 = [""] * largo

print("1-Accion, 2-Drama, 3-Comedia.")
genero=int(input("Seleccione: "))



