class libros:
    def __init__(self, cod, nombre, genero, estado):
        self.cod = cod
        self.nombre = nombre
        self.genero = genero
        self.estado = estado
    def __repr__(self):
        return "Cod:{0}, {1}, Genero:{2}, Estado:{3}".format(self.cod, self.nombre, self.genero, self.estado)

lstLibros = []
with open("Libros.txt" , "r") as arch:
    for linea in arch:
        a=linea.split("|")
        lstLibros.append(libros(int(a[0]), a[1], int(a[2]), int(a[3])))

    
"""
def Agregar(lstLibros):
    cod = int(input("Cod: "))
    nom = input("Nombre: ")
    print("1-Terror, 2-Poesia, 3-Drama.")
    gen = int(input("Genero: "))
    print("1-Libre, 2-Reservado.")
    est = int(input("Estado: "))
    lstLibros.append(libros(cod,nom,gen,est))
    print(lstLibros)
"""

def Reservar(lstLibros):
    ref = int(input("Cod: "))
    for i in range(0,len(lstLibros)):
        if lstLibros[i].cod == ref:
            lstLibros[i].estado = 2
            print("Libro:",lstLibros[i].nombre,"- RESERVADO.")
            
def EmitirOrd(lstLibros):
    for j in range(0,len(lstLibros)):
        for i in range(0,len(lstLibros)-1):
            if lstLibros[i].nombre.lower() > lstLibros[i+1].nombre.lower():
                aux = lstLibros[i]
                lstLibros[i] = lstLibros[i+1]
                lstLibros[i+1] = aux
                
    with open ("Libros Ordenados.txt","w+") as archivu:
        for i in range(0,len(lstLibros)):
            a = lstLibros[i]
            archivu.write("Cod:{0}, {1}, Genero:{2}, Estado:{3}\n".format(a.cod, a.nombre, a.genero, a.estado))
            
def EmitirRefCod(lstLibros):
    for j in range(0,len(lstLibros)):
        for i in range(0,len(lstLibros)-1):
            if lstLibros[i].cod > lstLibros[i+1].cod:
                aux = lstLibros[i]
                lstLibros[i] = lstLibros[i+1]
                lstLibros[i+1] = aux
                
    with open ("Libros Referencia.txt","w+") as archiv:
        for i in range(0,len(lstLibros)):
                a = lstLibros[i]
                archiv.write("Cod:{0},{1}, Genero:{2}, Estado:{3}\n".format(a.cod, a.nombre, a.genero, a.estado))
    print("# HECHO. #")
    
def Menu():
    print("1- Agregar Libro.")
    print("2- Reservar.")
    print("3- Emitir listado -Ord.")
    print("4- Emitir por ref. Cod.")
    print("0- Salir.")
    opc = int(input("Opción: "))
    return opc
opc = ""
while opc != 0:
    opc = Menu()
    if opc == 1:
        Agregar(lstLibros)
    if opc == 2:
        Reservar(lstLibros)
    if opc == 3:
        EmitirOrd(lstLibros)
    if opc == 4:
        EmitirRefCod(lstLibros)
        