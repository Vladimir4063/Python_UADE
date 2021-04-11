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
    print("Menu Vendedores")
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
        
        
        
#Productos
class Producto:
    def __init__(self, idProducto, descProducto, idCategoria, precio, stockActual):
        self.idProducto=idProducto
        self.descProducto=descProducto
        self.idCategoria=idCategoria
        self.precio=precio
        self.stockActual=stockActual

    def __repr__(self):
        return "%i, %s, %i, %i, %i" % (self.idCategoria, self.descProducto, self.idCategoria, self.precio, self.stockActual)
  
    
def menu():
    print("---------------------------------")
    print("Menu Producto")
    print("1-Alta")
    print("2-Buscar")
    print("3-Modificar")
    print("4-Baja")
    print("5-Salir")
    opc= int(input("Ingrese opcion: "))
    return opc





def BuscarProducto(producto, aBuscar, largo):
    for i in range(0, largo):
        if aBuscar == producto[i]:
            return i 
    return -1




def Alta(producto, desc, cat, precio, stock,largo):
    pos= BuscarProducto(producto, "", largo)
    if pos == -1:
        print("No hay espacios vacios para agregar un producto")
    else:
        producto[pos]= input("Ingrese un nuevo producto: ")
        desc[pos]= input("Ingrese una descripcion: ")
        cat[pos]= input("Ingrese una nueva categoria: ")
        precio[pos]= int(input("Ingrese un nuevo precio: "))
        stock[pos]= int(input("Ingrese cantidad de stock: "))
  
  
        
def Modificacion(producto, desc, cat, precio, stock,largo):
    productoABuscar= input("Ingrese producto a buscar: ")
    
    pos= BuscarProducto(producto, productoABuscar, largo)
    if pos == -1:
        print("producto no encontrado")
    else:
        producto[pos]= input("Ingrese el nuevo producto: ")
        desc[pos]= input("Ingrese la nueva descripcion: ")
        cat[pos]= input("Ingrese la nueva categoria: ")
        precio[pos]= int(input("Ingrese el nuevo precio: "))
        stock[pos]= int(input("Ingrese el nuevo stock: "))
  
  
  
def Baja (producto, desc, cat, precio, stock,largo):
    productoABuscar= input("Ingrese producto a buscar: ")
    
    pos= BuscarProducto(producto, productoABuscar, largo)
    if pos == -1:
        print("produto no encontrado")
    else:
        producto[pos]= "" 
        desc[pos]= ""
        cat[pos]= ""
        precio[pos]= 0 
        stock[pos]= 0
   
   
   
def Busqueda(producto, desc, cat, precio, stock,largo):
    productoABuscar= input("Ingrese producto a buscar: ")
    
    pos= BuscarProducto(producto, productoABuscar, largo)
    if pos == -1:
        print("producto no encontrado")
    else:
        print("producto: ", producto[pos])
        print("descripcion: ", desc[pos])
        print("categoria: ",cat[pos])
        print("precio: ", precio[pos])
        print("stock: ", stock[pos])



MAX= 100
producto= [""]*MAX
desc= [""] * MAX
cat= [""] * MAX
precio= [0] * MAX
stock= [0] * MAX

for i in range(0,MAX - 3):
    producto[i] = "producto"+str(i)
    desc[i]= "desc"+str(i)
    cat[i]= "cat"+str(i)
    precio[i]= random.random() * 100 
    stock[i]= random.random() * 100 
    
opc= 0
while opc != 5:
    opc= menu()
    
    if opc == 1:
        Alta(producto, desc, cat, precio, stock, MAX)
    if opc == 2:
        Busqueda(producto, desc, cat, precio, stock, MAX)
    if opc == 3:
        Modificacion(producto, desc, cat, precio, stock, MAX)
    if opc == 4:
        Baja(producto, desc, cat, precio, stock, MAX)


#Cliente
class Cliente:
    def __init__ (self, idCliente, nombre, email):
        self.idCliente = idCliente
        self.nombre = nombre
        self.email = email
        
    def __repr__(self):
        return "[%i, %s, %s]" % (self.idCliente, self.nombre, self.email)
    
def menu():
    print("---------------------------------")
    print("Menu Cliente")
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
    print("Menu Local")
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
        
        
