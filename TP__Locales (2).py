#locales
import random

class Local:
    def __init__ (self, local, desc):
        self.local=local
        self.desc=desc
        
    def __repr__(self):
        return "[%i, %s]" % (self.local, self.desc)
    
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

def Buscarlocal(local, aBuscar, largo):
    for i in range(0, largo):
        if aBuscar == local[i]:
            return i 
    return -1

def Alta(local, desc, largo):
    pos= Buscarlocal(local, "", largo)
    if pos == -1:
        print("No hay espacios vacios para agregar un local")
    else:
        local[pos]= input("Ingrese un nuevo local: ")
        desc[pos]= input("Ingrese una descripcion: ")
        

def Modificacion(local, desc, largo):
    localABuscar= input("Ingrese local a buscar: ")
    
    pos= Buscarlocal(local, localABuscar, largo)
    if pos == -1:
        print("local no encontrado")
    else:
        local[pos]= input("Ingrese el nuevo local: ")
        desc[pos]= input("Ingrese la nueva descripcion: ")
        
def Baja (local, desc, largo):
    localABuscar= input("Ingrese local a buscar: ")
    
    pos= Buscarlocal(local, localABuscar, largo)
    if pos == -1:
        print("local no encontrado")
    else:
        local[pos]= "" 
        desc[pos]= ""
            
def Busqueda(local,desc, largo):
    localABuscar= input("Ingrese local a buscar: ")
    
    pos= Buscarlocal(local, localABuscar, largo)
    if pos == -1:
        print("local no encontrado")
    else:
        print("local: ", local[pos])
        print("descripcion: ", desc[pos])
        

MAX= 10
local= [""]*MAX
desc= [""] * MAX


for i in range(0,MAX - 3):
    local[i] = "Local"+str(i)
    desc[i]= "desc"+str(i)
    
    
opc= 0
while opc != 5:
    opc= menu()
    
    if opc == 1:
        Alta(local, desc, MAX)
    if opc == 2:
        Busqueda(local,desc, MAX)
    if opc == 3:
        Modificacion(local,desc, MAX)
    if opc == 4:
        Baja(local,desc, MAX)