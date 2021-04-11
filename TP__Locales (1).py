#locales
import random

class Vendedores:
    def __init__ (self, vendedores, desc):
        self.vendedores=vendedores
        self.desc=desc
        
    def __repr__(self):
        return "[%i, %s]" % (self.vendedores, self.desc)
    
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

def Buscarvendedores(vendedores, aBuscar, largo):
    for i in range(0, largo):
        if aBuscar == vendedores[i]:
            return i 
    return -1

def Alta(vendedores, desc, largo):
    pos= Buscarvendedores(vendedores, "", largo)
    if pos == -1:
        print("No hay espacios vacios para agregar un vendedor")
    else:
        vendedores[pos]= input("Ingrese un nuevo vendedor: ")
        desc[pos]= input("Ingrese una descripcion: ")
        

def Modificacion(vendedores, desc, largo):
    vendedoresABuscar= input("Ingrese local a buscar: ")
    
    pos= Buscarvendedores(vendedores, vendedoresABuscar, largo)
    if pos == -1:
        print("local no encontrado")
    else:
        vendedores[pos]= input("Ingrese el nuevo vendedor: ")
        desc[pos]= input("Ingrese la nueva descripcion: ")
        
def Baja (vendedores, desc, largo):
    vendedoresABuscar= input("Ingrese vendedores a buscar: ")
    
    pos= Buscarvendedores(vendedores, vendeoresABuscar, largo)
    if pos == -1:
        print("vendedor no encontrado")
    else:
        local[pos]= "" 
        desc[pos]= ""
            
def Busqueda(vendedores,desc, largo):
    vendedoresABuscar= input("Ingrese vendedor a buscar: ")
    
    pos= Buscarvendedores(vendedores, vendedoresABuscar, largo)
    if pos == -1:
        print("vendedores no encontrado")
    else:
        print("vendedores: ", vendedores[pos])
        print("descripcion: ", desc[pos])
        

MAX= 10
#vendedores = ID
#desc= nombres
ID= [""]*MAX
vendedores= [""] * MAX


for i in range(0,MAX - 3):
    ID[i] = "ID"+str(i)
    vendedores[i]= "vendedores"+str(i)
    
    
opc= 0
while opc != 5:
    opc= menu()
    
    if opc == 1:
        Alta(ID, vendedores, MAX)
    if opc == 2:
        Busqueda(ID, vendedores, MAX)
    if opc == 3:
        Modificacion(ID, vendedores, MAX)
    if opc == 4:
        Baja(ID, vendedores, MAX)