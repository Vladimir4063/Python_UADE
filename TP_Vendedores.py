#vendedores
import random

class Vendedores:
    def __init__ (self, ID, nombre):
        self.ID=ID
        self.nombre=nombre
        
    def __repr__(self):
        return "[%i, %s]" % (self.ID, self.nombre)
    
def menu():
    print("---------------------------------")
    print("Menu")
    print("1-Alta")
    print("2-Buscar")
    print("3-Modificar")
    print("4-Baja")
    print("5-Salir")
    opc= int(input("Ingrese opcion: "))
    return opc

def BuscarID(ID, aBuscar, largo):
    for i in range(0, largo):
        if aBuscar == ID[i]:
            return i 
    return -1

def Alta(ID, nombre, largo):
    pos= BuscarID(ID, "", largo)
    if pos == -1:
        print("No hay espacios vacios para agregar un ID")
    else:
        ID[pos]= input("Ingrese un nuevo ID: ")
        nombre[pos]= input("Ingrese un nombre: ")
        

def Modificacion(ID, nombre, largo):
    IDABuscar= input("Ingrese ID a buscar: ")
    
    pos= BuscarID(ID, IDABuscar, largo)
    if pos == -1:
        print("ID no encontrado")
    else:
        ID[pos]= input("Ingrese el nuevo ID: ")
        nombre[pos]= input("Ingrese el nuevo nombre: ")
        
def Baja (ID, nombre, largo):
    IDABuscar= input("Ingrese ID a dar de baja: ")
    
    pos= BuscarID(ID, IDABuscar, largo)
    if pos == -1:
        print("ID no encontrado")
    else:
        ID[pos]= "" 
        nombre[pos]= ""
            
def Busqueda(ID, nombre, largo):
    IDABuscar= input("Ingrese ID a buscar: ")
    
    pos= BuscarID(ID, IDABuscar, largo)
    if pos == -1:
        print("ID no encontrado")
    else:
        print("ID: ", ID[pos])
        print("nombre: ", nombre[pos])
        

MAX= 10
ID= [""]*MAX
nombre= [""] * MAX


for i in range(0,MAX - 3):
    ID[i] = "ID"+str(i)
    nombre[i]= "nombre"+str(i)
    
    
opc= 0
while opc != 5:
    opc= menu()
    
    if opc == 1:
        Alta(ID, nombre, MAX)
    if opc == 2:
        Busqueda(ID, nombre, MAX)
    if opc == 3:
        Modificacion(ID, nombre, MAX)
    if opc == 4:
        Baja(ID, nombre, MAX)