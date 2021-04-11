
from tkinter import *

############################################# LLAMO FINAL

def ABMProd():
    import FINAL

#Creo los registros:

########################################################################## ABM Vendedores
#Creo los registros:
class Vendedor:
    def __init__(self, ID, nombre):
        self.ID=ID
        self.nombre=nombre
    def __repr__(self):
        return "{0}, {1}".format(self.ID, self.nombre)

lstVendedor = []
for i in range(0,5):
    lstVendedor.append(Vendedor(i + 1, "Vendedor " + str(i + 1)))
    

def AltaVendedor(entrada2):
    dec=entrada2.get
    lstVendedor.append(Vendedor(1 , dec))
    
    return dec
   
def printListaV(lstVendedor):
    for i in range(0,len(lstVendedor)):
        
        c = lstVendedor[i]
    return ("ID: {0} - {1}".format(c.ID, c.nombre))

def Vendedor():
    #Ventana grafica        
    vendedor=Toplevel()
    vendedor.title("Ventana 2")
    vendedor.geometry('400x380')
    vendedor.grab_set()
    lblVendedor=Label(vendedor, text="Vendedor")
    btnQuitar = Button(vendedor, text="Quitar", width=20, command= AltaVendedor)
    btnAgregar = Button(vendedor, text="Agregar", width=20, command= lambda: AltaVendedor(entrada2))
    btnSalir = Button(vendedor, text="Salir", width=20, command=vendedor.destroy)
    txtVendedor=Text(vendedor, width=20, height=6)
    texto=printListaV(lstVendedor)
    
    #Agregar
    lblDesc=Label(vendedor, text="Nombre") #Caja
    var=StringVar() # Envia
    entrada2=Entry(vendedor, textvariable=var) #Toma datos
    
    #Llamando funciones
    lblVendedor.pack()
    txtVendedor.pack()
    lblDesc.pack()
    entrada2.pack(padx=5, pady=5, ipadx=5, ipady=5)
    entrada2.focus()
    btnAgregar.pack()
    btnQuitar.pack()
    btnSalir.pack()
    txtVendedor.insert(END, texto)
    menu.wait_window(vendedor)


########################################################################## ABM Locales
#Creo los registros:
class Local:
    def __init__(self, ID, nombre):
        self.ID=ID
        self.nombre=nombre
    def __repr__(self):
        return "[Local: %i - %s]" % (self.ID, self.nombre)

lstLocal = []

for i in range(0,5):
    lstLocal.append(Local(i + 1, "Local " + str(i + 1)))
   


def AltaLocales(entrada1):
    desc=entrada1.get()
    lstLocal.append(Local(i + 1,desc))
    return desc

def Locales():
    #Ventana grafica
    texto= ""
    for i in range(0,len(lstLocal)):
        texto += lstLocal[i].nombre + "\r\n"
      
    locales=Toplevel()
    locales.title("Ventana 2")
    locales.geometry('400x380')
    locales.grab_set()
    lblLocales=Label(locales, text="Locales")

    var=StringVar()
    entrada1= Entry(locales, textvariable= var)


    btnQuitar = Button(locales, text="Quitar", width=20, command= AltaLocales)
    btnAgregar = Button(locales, text="Agregar", width=20, command= lambda: AltaLocales(entrada1))
    btnSalir = Button(locales, text="Salir", width=20, command=locales.destroy)
    txtLocales=Text(locales, width=20, height=6)
    
    #Agregar
    lblDesc=Label(locales, text="Descripción")
    
    
    #Llamando funciones
    lblLocales.pack()
    txtLocales.pack()
    lblDesc.pack()
    entrada1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    btnAgregar.pack()
    btnQuitar.pack()
    btnSalir.pack()
    txtLocales.insert(END, texto)
    menu.wait_window(locales)
    
################################################################################## Menu
class CategoriaPr():
    def __init__(self, ID, categoria):
        self.ID=ID
        self.categoria=categoria
    def __repr__(self):
        return "[Categoria: %i - %s]" % (self.ID, self.categoria)

lstCategoriaPr = []
for i in range(0,5):
    lstCategoriaPr.append(CategoriaPr(i + 1, "Categoria " + str(i + 1)))
    
contadoryID = 1

def AltaCategoriaPr():
    nombre=(entrada1.get)
    lstCategoriaPr.append(nombre)
    
    contadorID = contadorID + 1
    return contadorID
    
def CategoriaPr():
    #Ventana grafica
    
    texto= ""
    for i in range(0,len(lstCategoriaPr)):
        texto += lstCategoriaPr[i].categoria + "\r\n"
        
    categoriaPr=Toplevel()
    categoriaPr.title("Ventana 2")
    categoriaPr.geometry('400x380')
    categoriaPr.grab_set()
    lblCategoriaPr=Label(CategoriaPr, text="Categoria Prod.")
    btnQuitar = Button(categoriaPr, text="Quitar", width=20, command= AltaCategoriaPr)
    btnAgregar = Button(categoriaPr, text="Agregar", width=20, command= AltaCategoriaPr)
    btnSalir = Button(categoriaPr, text="Salir", width=20, command=Al.destroy)
    txtcategoriaPr=Text(categoriaPr, width=20, height=5)
    
    #Agregar
    lblDesc=Label(categoriaPr, text="Nombre")
    var=StringVar()
    entrada1=Entry(categoriaPr, textvariable = var)
    
    #Llamando funciones
    lblCategoriaPr.pack()
    txtcategoriaPr.pack()
    lblDesc.pack()
    entrada1.pack(padx=5, pady=5, ipadx=5, ipady=5)
    btnAgregar.pack()
    btnQuitar.pack()
    btnSalir.pack()
    txtcategoriaPr.insert(END, texto)
    menu.wait_window(categoriasPr)
    
############################################################################################ M E N U .

def Menu():
    menu.title("Software")
    menu.geometry('400x350')
    etiqueta1=Label(menu, text="Menu")
    locales=Button(menu, text= "Locales", width=20, command=Locales)
    vendedores=Button(menu, text= "Vendedores", width=20, command=Vendedor)
    categoriasPr=Button(menu, text= "Categoria Prod.", width=20, command=ABMProd)
    cerrar=Button(menu, text= "Cerrar", width=20, command=menu.destroy) #Boton cerrar.
    
    etiqueta1.pack()                          
    locales.pack()
    vendedores.pack()
    categoriasPr.pack()
    cerrar.pack()
    menu.mainloop()
menu = Tk()
Menu()
