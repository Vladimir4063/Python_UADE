class Libros:
    def __init__(self,codigo,nombre,genero,estado):
        self.codigo = codigo
        self.nombre = nombre
        self.genero = genero
        self.estado = estado
    
    def __repr__(self):
        return "{0} | {1} | {2} | {3}".format(self.codigo,self.nombre,self.genero,self.estado)
    
lstLibros = []

"""
with open("Libros.txt","r") as archivo:
    for linea in archivo:
        a = linea.split("|")
        lstLibros.append(Libros(int(a[0]),a[1],int(a[2]),int(a[3])))
"""

def menu():
    print("1)Agregar Libro")
    print("2)Reservar Libro")
    print("3)Ordenar en orden alfabetico")
    print("4)Ordenar por codigo(mayor a menor)")
    valido = False
    while valido == False:
     try:
       opc = int(input("Ingrese opcion: "))
       if opc < 0 or opc > 4:
           raise Exception("Opcion incorrecta")
       valido = True
       
     except ValueError:
         print("No se aceptan letras")
     except Exception as error:
         print(error.args[0])

         
    return opc

def Reservar(lstLibros):
    nro = int(input("Ingrese codigo de libro: "))
    for i in range(0,len(lstLibros)):
        if lstLibros[i].codigo == nro:
            lstLibros[i].codigo = 2
            print("El estado del libro",lstLibros[i].nombre,"es ocupado")
            return
        
    print("No se ha encontrado el libro")
    return

def OrdenAlfabetico(lstLibros):
    for j in range(0,len(lstLibros)):
        for i in range(0,len(lstLibros)-1):
            if lstLibros[i].nombre.lower() > lstLibros[i+1].nombre.lower():
                aux = lstLibros[i]
                lstLibros[i] = lstLibros[i+1]
                lstLibros[i+1] = aux
                
    with open("ListaOrdenada.txt","w+") as arch:
        for i in range(0,len(lstLibros)):
            arch.write("{0} - {1} - {2} - {3}\n".format(lstLibros[i].codigo,lstLibros[i].nombre,lstLibros[i].genero,lstLibros[i].estado))

def Agregar(lstLibros):
    cod = input("Cod. del libro: ")
    nom = input("Nombre del libro: ")
    genero = int(input("Ingrese genero del libro: 1)Terror o 2) Poesia o 3) Drama: "))
    estado = int(input("Ingrese estado del libro: 1)Libre o 2)Reservado: "))
    lstLibros.append(Libros(cod,nom,genero,estado))
    
def Ordenar(lstLibros):
    for j in range(0,len(lstLibros)):
        for i in range(0,len(lstLibros)-1):
            if lstLibros[i].codigo < lstLibros[i+1].codigo:
                aux = lstLibros[i+1]
                lstLibros[i+1] = lstLibros[i]
                lstLibros[i] = aux
            
    for i in range(0,len(lstLibros)):
        print(lstLibros[i])

opc = ""
while opc != 0:
    opc = menu()
    if opc == 1:
        Agregar(lstLibros)
    if opc == 2:
        Reservar(lstLibros)
    if opc == 3:
        OrdenAlfabetico(lstLibros)
    if opc == 4:
        Ordenar(lstLibros)