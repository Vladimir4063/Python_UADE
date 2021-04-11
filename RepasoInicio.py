class reuniones:
    def __init__(self, place, users, theme, duration):
        self.place = place
        self.users = users
        self.theme = theme
        self.duration = duration
    def __repr__(self):
        return "[%i, %s, %s]" % (self.place, self.users, self.theme, self.duration)
    
    
    
listEvents = []
proximoID = 0

def addMembers():
    cant = int(input("Cant: "))
    listCant = [] * cant
    nameComplet = input("Complet name: ")
    return
    

def altaReunion(listEvents, proximoID):
    place = input("Place: ")
    members = []
    users = input("Name: ")
    theme = input("Theme: ")
    print("# Duration in minutes: 1- 30', 2-60', 3-Undefined #")
    duration = int(input("Opc: "))
    newReu = reuniones(place, users, theme, duration)
    listEvents.append(newReu)
    proximoID = proximoID + 1
    return

txt = """
1-Registrar Reunion
0-Salir.
"""

op = ""
while op !=0:
    print(txt)
    op = int(input("Ingrese Opción: "))
    if op == 1:
        altaReunion(listEvents, proximoID)
        
