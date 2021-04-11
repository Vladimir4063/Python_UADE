class departamentos:
    def __init__(self, nro, desc, m2, estado, precio):
        self.nro = nro
        self.desc = desc
        self.m2 = m2
        self.estado = estado
        self.precio = precio
    def __repr__(self):
        return "{0}, {1}, M2:{2}, Estado: {3}, ${4}".format(self.nro, self.desc, self.m2, self.estado, self.precio)

lstDepartamentos = []

with open ("Dept.txt","r") as arch:
    for linea in arch:
        a=linea.split(",")
        lstDepartamentos.append(departamentos(int(a[0]), a[1], int(a[2]), int(a[3]), float(a[4])))

def Reservas(lstDepartamentos):
    nroDp = int(input("Nro. Dept: "))
    for i in range(0,len(lstDepartamentos)):
        if lstDepartamentos[i].nro == nroDp:
            lstDepartamentos[i].estado = 1
            lstDepartamentos[i].precio = int(input("Precio pactado: "))
            return
    print("## No se encontro departamento ##")
    return

def EmitirList(lstDepartamentos):
    for j in range(0,len(lstDepartamentos)):
        for i in range(0,len(lstDepartamentos)-1):
            if lstDepartamentos[i].m2 > lstDepartamentos[i+1].m2:
                aux = lstDepartamentos[i+1]
                lstDepartamentos[i+1] = lstDepartamentos[i]
                lstDepartamentos[i] = aux
                 
    with open ("DepartamentosOrdenados.txt", "w+") as arch2:
        for i in range(0,len(lstDepartamentos)):
            a = lstDepartamentos[i]
            if lstDepartamentos[i].estado == 1:
                arch2.write("{0}, {1}, M2:{2}, Estado: {3}, ${4}\n".format(a.nro, a.desc, a.m2, a.estado, a.precio))
        
def Informe(lstDepartamentos):
    vec = [0] * 4
    for i in range(0,len(lstDepartamentos)):
        aux = lstDepartamentos[i].estado
        vec[aux] = vec[aux]+1
    print("Estado 1: ", vec[1])
    print("Estado 2: ", vec[2])
    print("Estado 3: ", vec[3])
    
def Guardar(lstDepartamentos):
    with open ("DepartamentosGuardados.txt", "w+") as archivu:
        for i in range(0,len(lstDepartamentos)):
            a = lstDepartamentos[i]
            archivu.write("{0}, {1}, M2:{2}, Estado: {3}, ${4}\n".format(a.nro, a.desc, a.m2, a.estado, a.precio))
    
def Menu():
    print("1- Reservar Dept.")
    print("2- Emitir listado.")
    print("3- Informe.")
    print("4- Guardar")
    print("0- Salir.")
    opc=int(input("Opción: "))
    return opc
opc = ""
while opc !=0:
    opc = Menu()
    if opc == 1:
        Reservas(lstDepartamentos)
    if opc == 2:
        EmitirList(lstDepartamentos)
    if opc == 3:
        Informe(lstDepartamentos)
    if opc == 4:
        Guardar(lstDepartamentos)

print(lstDepartamentos)
        