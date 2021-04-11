from tkinter import *

def imp():
    import TPprogra
    
def Fecha():
    import time
    hora=time.strftime("%x")
    a = hora
    return a

def Buscar():
    with open('vendedor.csv', 'r', encoding='utf-8') as csv:
        for linea in csv:
            return (linea)

    
def Factura():
    
    Factura=Toplevel()
    Factura.title("Factura")
    Factura.geometry('400x600')
    Int= IntVar
    txtFactura=Text(Factura, width=30, height=10)
    etiqueta1=Label(Factura, text="Nro. de factura")
    Nro=Entry(Factura, textvariable= Int)
    etiqueta2=Label(Factura, text="ID Vendedor")
    IDvendedor=Entry(Factura, textvariable= Int)
    etiqueta3=Label(Factura, text="ID Local")
    IDlocal=Entry(Factura, textvariable= Int)
    etiqueta4=Label(Factura, text="ID Cliente")
    IDcliente=Entry(Factura, textvariable= Int)
    agregar=Button(Factura, text="Buscar", width=20)
    salir=Button(Factura, text= "Cerrar", width=20, command=Factura.destroy)

    
    etiqueta1.pack()
    Nro.pack()
    etiqueta2.pack()
    IDvendedor.pack()
    etiqueta3.pack()
    IDlocal.pack()
    etiqueta4.pack()
    IDcliente.pack()
    agregar.pack()
    txtFactura.pack()
    txtFactura.insert(END, Buscar()) 
    salir.pack()

def Menu():
    menu.title("Software")
    menu.geometry('400x350')
    etiqueta1=Label(menu, text="Menu")
    Listas=Button(menu, text= "Listas", width=20, command=imp)
    Facturas=Button(menu, text= "Facturas", width=20, command=Factura)
    cerrar=Button(menu, text= "Cerrar", width=20, command=menu.destroy)
    
    etiqueta1.pack()                          
    Listas.pack()
    Facturas.pack()
    cerrar.pack()
    menu.mainloop()
menu = Tk()
Menu()