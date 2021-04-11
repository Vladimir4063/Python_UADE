# Comercio

class productos:
    def __init__(self, cod, nom, cat, pre, est):
        self.cod = cod
        self.nom = nom
        self.cat = cat
        self.pre = pre
        self.est = est

    def __repr__(self):
        return "Cod:{0}, {1}, Ctg:{2}, $:{3}, Est:{4}\n".format(self.cod, self.nom, self.cat, self.pre, self.est)


lstProduc = []

with open("Productos.txt", "r") as arch:
    for linea in arch:
        a = linea.split(",")
        lstProduc.append(
            productos(int(a[0]), a[1], int(a[2]), int(a[3]), int(a[4])))


def Agregar(lstProduc):
    cod = int(input("Cod: "))
    nom = input("Nombre: ")
    print("1-Almacen, 2-Fiambreria, 3-Carniceria.")
    cat = int(input("Categoria: "))
    pre = int(input("Precio: "))
    print("1-Vendido, 2-Disponible.")
    est = int(input("Estado: "))
    lstProduc.append(productos(cod, nom, cat, pre, est))
    print("############### ¡HECHO! #################")
    print("#########################################")
    return


def SelecVendidos(lstProduc):
    ref = input("Producto: ")
    for i in range(0, len(lstProduc)):
        if lstProduc[i].nom == ref:
            lstProduc[i].est = 1
            print("Prod: ", lstProduc[i].nom, "seleccionado como VENDIDO.")


def EmitirOrd1(lstProduc):
    for j in range(0, len(lstProduc)):
        for i in range(0, len(lstProduc)-1):
            if lstProduc[i].nom.lower() > lstProduc[i+1].nom.lower():
                aux = lstProduc[i]
                lstProduc[i] = lstProduc[i+1]
                lstProduc[i+1] = aux

    with open("Orden alfabetico.txt", "w+") as arch:
        for i in range(0, len(lstProduc)):
            a = lstProduc[i]
            arch.write("Cod:{0}, {1}, Ctg:{2}, $:{3}, Est:{4}\n".format(
                a.cod, a.nom, a.cat, a.pre, a.est))


def EmitirOrd2(lstProduc):
    for j in range(0, len(lstProduc)):
        for i in range(0, len(lstProduc)-1):
            if lstProduc[i].pre > lstProduc[i+1].pre:
                aux = lstProduc[i]
                lstProduc[i] = lstProduc[i+1]
                lstProduc[i+1] = aux

    with open("Orden numerico.txt", "w+") as arch1:
        for i in range(0, len(lstProduc)):
            a = lstProduc[i]
            arch1.write("Cod:{0}, {1}, Ctg:{2}, $:{3}, Est:{4}\n".format(
                a.cod, a.nom, a.cat, a.pre, a.est))


def Precios(lstProduc):
    item = input("Producto: ")
    for i in range(0, len(lstProduc)):
        if lstProduc[i].nom == item:
            oldPrice = lstProduc[i].pre
            print("Old Price:", oldPrice)
            newPrice = int(input("New Price: "))
            lstProduc[i].pre = newPrice
            print("############### ¡HECHO! #################")
            print("#########################################")
            return


def AumentoCatg(lstProduc):
    print("¡ATENCIÓN! Se incrementara el 10% a dicha categoria.")
    ctg = int(input("Ingrese categoria."))
    for i in range(0, len(lstProduc)):
        if lstProduc[i].cat == ctg:
            pre = lstProduc[i].pre
            fin = pre * 1.10
            lstProduc[i].pre = fin

    for i in range(0, len(lstProduc)):
        print("Precios Actualizados:")
        print(lstProduc[i])


def Buscador(lstProductos):
    carac = input("Ingrese caracter a Buscar:")
    caracter = carac.upper()  # Convierte la primer letra en Mayúscula.
    for i in range(0, len(lstProduc)):
        if lstProduc[i].nom[0:1] == caracter:
            print(lstProduc[i])
            print("################")


def lista(lstProduc):
    print(lstProduc)


def Menu():
    print("1-Agregar prod.")
    print("2-Selec. Vendidos.")
    print("3-Emitir prod. en orden alfabetico.")
    print("4-Emitir prod. en orden numérico.")
    print("5-Modificar Precio.")
    print("6-Incrementar 10%.")
    print("7-Buscador.")
    print("8-Imprimir Lista.")
    print("0-Salir.")
    opc = int(input("Opción: "))
    return opc


opc = ""
while opc != 0:
    opc = Menu()
    if opc == 1:
        Agregar(lstProduc)
    if opc == 2:
        SelecVendidos(lstProduc)
    if opc == 3:
        EmitirOrd1(lstProduc)
    if opc == 4:
        EmitirOrd2(lstProduc)
    if opc == 5:
        Precios(lstProduc)
    if opc == 6:
        AumentoCatg(lstProduc)
    if opc == 7:
        Buscador(lstProduc)
    if opc == 8:
        lista(lstProduc)
