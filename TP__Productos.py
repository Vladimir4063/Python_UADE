import random 

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
    print("Menu")
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

