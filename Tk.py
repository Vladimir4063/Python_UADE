from tkinter import *
from tkinter import ttk

lstLocales =[""]*16


def agrega(entrada):
    lstLocales.insert(END,entrada.get())
    
def borrar():
    b = lstLocales.curselection()
    if(b != ""):
        lstLocales.delete(b)    
    
def AltaBaja():    
    root=Toplevel()
    root.geometry("720x580")
    root.iconbitmap("BOLI.ico")
    root.title("Lista De Locales")
    root.grab_set()
    lblLocales=Label(root,text="Lista de locales:").place(x=100,y=90)           
    #Creando una Lista
    lstLocales=Listbox(root,width=50)
    lstLocales.place(x=100,y=120)
    lblLoc=Label(root,text="Local:").place(x=100,y=20)
    entrada=StringVar()
    textentrada=Entry(root,textvariable=entrada,width=40).place(x=150,y=20)
    btnAgregar=Button(root,text="Dar de Alta",height=2,width=15,command=agrega(entrada)).place(x=360,y=430)
    btnAgregar=Button(root,text="Dar de Baja",height=2,width=15,).place(x=170,y=430)
    root.mainloop()

def lstVendedores():    
    root= Toplevel()
    root.geometry("720x580")
    root.iconbitmap("BOLI.ico")
    root.title("Lista De vendedores")
    root.grab_set()
    lblVendedores=Label(root,text="Lista de Vendedores:").place(x=100,y=90)           
    #Creando una Lista
    lstVendedores=Listbox(root,width=50)
    lstVendedores.place(x=100,y=120)
    lbltext=Label(root,text="Vendedor: ").place(x=100,y=20)
    entrada=StringVar()
    txtLocal=Entry(root,textvariable=entrada,width=40).place(x=200,y=20)
    btnAgregar=Button(root,text="Añadir",height=2,
                      width=15,command=agrega).place(x=360,y=430)
    btnAgregar=Button(root,text="Quitar",height=2,
                      width=15,).place(x=170,y=430)
    root.mainloop()




def GUI():
    raiz = Tk()
    raiz.iconbitmap("BOLI.ico")
    raiz.geometry('380x300')
    raiz.configure(bg='sandy brown')
    raiz.title('Programa de Gestion')
    Intro=ttk.Label(raiz, text="Zapateria # El Rinconzito #", font=(32))
    Intro.pack(fill=tk.X, ipadx=20, ipady=20, padx=20, pady=20)
    
    lta=ttk.Button(raiz, text='Lista de locales',command=AltaBaja)
    lta.grid(row=3, column=1, padx=10, pady=10)
    bja=ttk.Button(raiz, text='Lista de vendedores',command=lstVendedores)
    bja.grid(row=4, column=1, padx=10, pady=10)
    Fin=ttk.Button(raiz, text='Salir', command=raiz.destroy)
    Fin.grid(row=5, column=1, padx=10, pady=10)
    raiz.mainloop()


GUI()
