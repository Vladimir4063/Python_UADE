#locales
import random

class Local:
    def __init__ (self, idCliente, nombre, email):
        self.idCliente = idCliente
        self.nombre = nombre
        self.email = email
        
    def __repr__(self):
        return "[%i, %s, %s]" % (self.idCliente, self.nombre, self.email)
    
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

def BuscarCliente(idCliente, aBuscar, largo):
    for i in range(0, largo):
        if aBuscar == idCliente[i]:
            return i 
    return -1

def Alta(idCliente,nombre, email, largo):
    pos = BuscarCliente(idCliente, "", largo)
    if pos == -1:
        print("No hay espacios vacios para agregar un cliente")
    else:
        idCliente[pos]= input("Ingrese un nuevo idCliente: ")
        nombre[pos]= input("Ingrese un nombre: ")
        email[pos]= input("Ingrese el email: ")
        

def Modificacion(idCliente,nombre, email, largo):
    ClienteABuscar = input("Ingrese cliente a buscar: ")
    
    pos= BuscarCliente(idCliente, ClienteABuscar, largo)
    if pos == -1:
        print("cliente no encontrado")
    else:
        idCliente[pos]= input("Ingrese el nuevo idCliente: ")
        nombre[pos]= input("Ingrese el nuevo nombre: ")
        email[pos]= input("Ingrese el nuevo email: ")
        
def Baja (idCliente,nombre, email, largo):
    ClienteABuscar = input("Ingrese idCliente a buscar: ")
    
    pos = BuscarCliente(idCliente, ClienteABuscar, largo)
    if pos == -1:
        print("cliente no encontrado")
    else:
        idCliente[pos]= "" 
        nombre[pos]= ""
        email[pos]= ""
        
def Busqueda(idCliente,nombre, email, largo):
    ClienteABuscar = input("Ingrese cliente a buscar: ")
    
    pos = BuscarCliente(idCliente, ClienteABuscar, largo)
    if pos == -1:
        print("cliente no encontrado")
    else:
        print("cliente: ", idCliente[pos])
        print("nombre: ", nombre[pos])
        print("email: ", email[pos])
        

MAX = 10
idCliente = [""]* MAX
nombre = [""] * MAX
email = [""]* MAX


for i in range(0,MAX - 3):
    idCliente[i] = "cliente"+str(i)
    nombre[i]= "nombre"+str(i)
    email[i]= "email"+str(i)
    
opc= 0
while opc != 5:
    opc= menu()
    
    if opc == 1:
        Alta(idCliente, nombre, email, MAX)
    if opc == 2:
        Busqueda(idCliente, nombre, email, MAX)
    if opc == 3:
        Modificacion(idCliente, nombre, email, MAX)
    if opc == 4:
        Baja(idCliente, nombre, email, MAX)