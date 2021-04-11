# Crea un programa que al iniciar te pregunte que carrera deseas. Luego te de información de la misma. Luego te consulte que
# tamaño debe ser una lista y busca su numero mayor.
import random
text = """ *** ¿Que carrera eliges?
           *** 1 - Abogado.
           *** 2 - Defensor.
           """
print(text)

num = int(input("Respuesta: "))
if num == 1:
    print("""El abogado es el profesional que ejerce la defensa jurídica en un juicio, así como los procesos judiciales y administrativos ocasionados o sufridos por ella.​ Además, asesora y da consejo en materias jurídicas.""")
if num == 2:
    print("""Como idea general, un defensor es una persona que protege algo, lo defiende de una posible amenaza.""")
    
MAX = int(input("Tamaño de lista: "))
lista = [0] * MAX
for i in range(0,MAX):
    lista[i] = random.randint(1,90)
    
Mayor = 0
for i in range(0,len(lista)):
    if lista[i] > Mayor:
        Mayor = i
print("Numero mayor: ", Mayor)