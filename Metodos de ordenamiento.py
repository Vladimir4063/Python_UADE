#Ordenar vector de mayor a menor
vector = [10,11,1,49,53,120,76,190,92,101] #Definimos el vector


print("Vector Desordenado")
print(vector)

for j in range(0,len(vector)):     #Corremos el vector utilizando 2 for i in range
  for i in range(0,len(vector)-1): #Le restamos 1 al segundo for y comparamos:
      if vector[i] < vector[i+1]:  #Si el vector en la posicion vector[i] (10) <(es menor) que el vector[i+1](11)
          aux = vector[i+1]        #Creamos una variable auxiliar para guardar el dato de vector[i+1] (11)
          vector[i+1] = vector[i]  #Ahora el vector en la posicion [i+1] sera igual al valor del vector en la posicion [i] que es: 10 (Se intercambiar las posiciones)
          vector[i] = aux          #Ahora el vector en la posicion [i] sera igual a la variable auxiliar que creamos, en este caso es 11 (Se intercambiar las posiciones)
                                   #Esto se repite hasta la longitud de la lista y de esta manera se ordena de mayor a menor        
print("Vector Ordenado")                               
print(vector)


#Ordenar vector de menor a mayor:
for j in range(0,len(vector)):     
  for i in range(0,len(vector)-1):  #Para ordenar un vector de menor a mayor lo que hay que hacer es:
      if vector[i] > vector[i+1]:   #Cambiar la boca (antes era <, ahora es >) y es lo mismo al anterior.
          aux = vector[i+1]        
          vector[i+1] = vector[i]  
          vector[i] = aux
          
print("Vector ordenado de menor a mayor")
print(vector)

#Ordenar FILAS de la matriz de mayor a menor:
matriz = [[30,20,10],[20,150,200],[45,46,8]] #Definimos matriz
print(matriz)
for i in range(0,3):       #Utilizamos 3 for y al ultimo le restamos 1
  for f in range(0,3):
    for c in range(0,3-1):
        if matriz[f][c] < matriz[f][c+1]:  #Esta parte es igual a ordenar el vector de mayor a menor
            aux = matriz[f][c+1]           #Pero en este caso la matriz tiene fila y columnas
            matriz[f][c+1] = matriz[f][c]  # Y debemos recorrer ambas.
            matriz[f][c] = aux

print(matriz)
"""
#Ordenar apellidos por orden alfabetico:

#Este no funciona porque necesita una lista para comparar pero sirve como ejemplo:
for i in range(0,len(lstPostulantes)-1):  #Recorremos la lista
        if lstPostulantes[i].apellido.lower() > lstPostulantes[i+1].apellido.lower(): #Buscar el funcionamiento del .lower(basicamente compara la primer letras de los apellidos)
            aux = lstPostulantes[i].apellido  #Guardamos el apellido con valor "menor" en un auxiliar
            lstPostulantes[i].apellido = lstPostulantes[i+1].apellido #Sustituimos las posiciones como si fuese un vector
            lstPostulantes[i+1].apellido= aux
"""