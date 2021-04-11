#Ejercicio 1
import random
"""
MAX = int(input("Largo: "))
vector = [0] * MAX
for i in range(0,MAX):
    vector[i] = random.randint(0,80)

def funcion(vector,MAX):
    mayor = 0
    for i in range(0,len(vector)):
        if vector[i] % 2 == 0 and vector[i] > mayor:
            mayor = vector[i]
    return mayor

llamador = funcion(vector, MAX)
print(llamador)
"""            
#Ejercicio 2
"""
f = int(input("Cant. fila: "))
matriz = [[0] * 3 for i in range(0,f)] # Crea 3, y lo repite f(cant) de veces. Uno debajo del otro.

for fila in range(0,f):
    for colum in range(0,3):
        matriz[fila][colum] = random.randint(0,50)#La matriz, siempre son dos valores, filas y columnas.
        
for fila in range(0,f):
    for colum in range(0,3):
        print(matriz[fila][colum], end = " ")
    print()
    
num = int(input("Num. : "))

def Buscar(num,matriz,f):
    fi = ""
    col = ""
    for fila in range(0,f):
        for colum in range(0,3):
            if matriz[fila][colum] == num:
                fi = fila
                col = colum
            
                print("Fila: ", fi,"Columna: ",col)

    if fi == "" and col == "": # Creamos condicion para devolver -1. 
        return -1
    
a=Buscar(num,matriz,f)
if a == -1: #Si el valor no existe, regresa -1.
    print("-1")
"""
#Ejercicio 3
"""
largo = int(input("Largo: "))               
nombre = [""] * largo
#for i in range(0,largo):
    #nombre[i] = "Usuario" + str(i) #Carga la lista con nombres.
for i in range(0,largo):
    nombre[i]=input("Nombre: ")
    
nom = input("Ingrese nombre: ")
def Buscar1(nom,nombre,largo):
    for i in range(0,largo):
        if nombre[i] == nom:
            pos = i
            print("Posición es: ", pos)
a=Buscar1(nom,nombre,largo)
"""

#Ejercicio 4

class peliculas:
    def __init__(self, nombre, año, genero):
        self.nombre = nombre
        self.año = año
        self.genero = genero
    def __repr__(self):
        return "{0} | {1} | {2}".format(self.nombre, self.año, self.genero)
    
lstPeliculas = []

with open ("Peliculas.txt", "r") as arch:
    for linea in arch:
        a=linea.split("|")
        lstPeliculas.append(peliculas(a[0],a[1],int(a[2]))) #Transforma el numero a entero, debido a que comparaba texto a entero.
        
#for j in range(0,len(lstPeliculas)): #Imprime la lista.
    #print(lstPeliculas[j])
      
print("1-Acción, 2-Drama, 3-Comedia")
genero = int(input("Genero: "))

def Buscar2(lstPeliculas, genero):
    with open("NuevoPeliculas.txt", "w") as archivo:
        for i in range(0,len(lstPeliculas)):
            if lstPeliculas[i].genero == genero:               #"\n" hace un espacio al final (imprime abajo.)
                archivo.write(" {0} | {1} | {2}\n".format(lstPeliculas[i].nombre, lstPeliculas[i].año, lstPeliculas[i].genero))
a=Buscar2(lstPeliculas, genero)


def Buscar2(lstPeliculas, genero):
    with open("NuevoPeliculas.txt", "w") as archivo:
        for i in range(0,len(lstPeliculas)):
            if lstPeliculas[i].genero == genero: #"\n" hace un espacio al final (imprime abajo.)
                p = lstPeliculas[i]
                archivo.write(" {0} | {1} | {2}\n".format(p.nombre, p.año, p.genero))
a=Buscar2(lstPeliculas, genero)

#Ejercicio 5
"""
with open ("Pelis.csv", "w+") as archiv:
    for i in range(0,len(lstPeliculas)):
        p = lstPeliculas[i]
        archiv.write(" {0} | {1} | {2}\n".format(p.nombre, p.año, p.genero))
"""

#Ejercicio Integrador
"""
class departamentos:
    def __init__(self, numero, desc, metros, estado, precio):
        self.numero = numero
        self.desc = desc
        self.metros = metros
        self.estado = estado
        self.precio = precio
    def __repr__(self):
        return "{0}, {1}, {2}, {3}, ${4}".format(self.numero, self.desc, self.metros, self.estado, self.precio)
    
lstDepartamentos = []

def Leer(lstDepartamentos):
    with open("Dept.txt", "r") as archivu:
        for linea in archivu:
            a=linea.split(",")
            lstDepartamentos.append(departamentos(int(a[0]),a[1], int(a[2], int(a[3],a[4]))))

def Menu():
    print("1- Leer archivo.")
    print("2- Marcar Dept. reservado.")
    print("3- Emitir listado.")
    print("4- Informar detalles.")
    print("5- Guardar archivo.")
    opc = int(input("Opcion: "))
    return opc
opc = ""
while opc != 0:
    opc = Menu()
    if opc ==1:
        Leer(lstDepartamentos)
"""
        