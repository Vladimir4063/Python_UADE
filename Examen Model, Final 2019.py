class postulantes:
    def __init__(self, apellido, nombre, puesto, cod):
        self.apellido = apellido
        self.nombre = nombre
        self.puesto = puesto
        self.cod = cod
    def __repr__(self):
        return "{0} {1} {2} {3}".format(self.apellido, self.nombre, self.puesto, self.cod)
    
lstPostulantes = []

# r : read (leer), w : write (escribir) w+ : crea directamente el archivo.
with open ("OrdenarLstApellido.txt", "r") as arch:
    for linea in arch: #Por cada linea del archivo:
        a=linea.split(" ")
        lstPostulantes.append(postulantes(a[0], a[1], a[2], int(a[3])))
        
"""Imprime la lista que lee.
for i in range(0,len(lstPostulantes)):
    print(lstPostulantes[i])
"""
print("##################################")
def OrdenarApe(lstPostulantes):
    for j in range(0,len(lstPostulantes)):
        for i in range(0,len(lstPostulantes)-1):
            if lstPostulantes[i].apellido.lower() > lstPostulantes[i+1].apellido.lower(): #Tomamos el mayor para guardarlo. E intercambiar posiciones.
                aux = lstPostulantes[i]
                lstPostulantes[i] = lstPostulantes[i+1]
                lstPostulantes[i+1] = aux
                
                #aux = lstPostulantes[i].apellido
                #lstPostulantes[i].apellido = lstPostulantes[i+1].apellido
                #lstPostulantes[i+1].apellido = aux
    print("###################################")           
    for i in range(0,len(lstPostulantes)):
        print(lstPostulantes[i])
    print("###################################")

def FiltrarApe(lstPostulantes):
    print("Cod: *1, *2, *3, *4, *5.")
    ref = int(input("Cod. referencia: "))
    with open ("Apellido Ordenado.txt", "w+") as archivu:
        for i in range(0,len(lstPostulantes)):
            if lstPostulantes[i].cod == ref:
                a = lstPostulantes[i]
                archivu.write("{0} {1} {2} {3}\n".format(a.apellido, a.nombre, a.puesto, a.cod))

def CantRef(lstPostulantes):
    for j in range(0,len(lstPostulantes)):#ATENCION: Funcion no terminada.
        aux = 0
        for i in range(0, len(lstPostulantes)):
            if lstPostulantes[j].cod == lstPostulantes[i].cod:
                aux = aux + 1
        print("Cantidad de cod: ", lstPostulantes[j].cod, "es :", aux) #ATENCION: Funcion no terminada.
        
    lista = [0] * 5    
    for i in range(0,len(lstPostulantes)-1):
        aux = lstPostulantes[i].cod
        lista[aux] = lista[aux] + 1
    print("Cant. de codes: ", lista[0])#ATENCION: Funcion no terminada.

def agregarPost(lstPostulantes):
    ape = input("Apellido: ")
    nom = input("Nombre: ")
    pue = input("Puesto: ")
    cod = int(input("Cod: "))
    lstPostulantes.append(postulantes(ape,nom,pue,cod))
    
def Menu():
    print("1- Nuevo postulante.")
    print("2- Emitir listado.")
    print("3- Filtrar por codigo.")
    print("4- Cant. de postulantes.")
    print("0- Salir.")
    opc = int(input("Opción: "))
    return opc
opc = ""
while opc != 0:
    opc = Menu()
    if opc == 1:
        agregarPost(lstPostulantes)
    if opc == 2:
        OrdenarApe(lstPostulantes)
    if opc == 3:
        FiltrarApe(lstPostulantes)
    if opc == 4:
        CantRef(lstPostulantes)

with open ("OrdenarLstApellido.txt", "w") as arch:
    for i in range(0,len(lstPostulantes)):
        a = lstPostulantes[i]
        arch.write("{0} {1} {2} {3}\n".format(a.apellido, a.nombre, a.puesto, a.cod))