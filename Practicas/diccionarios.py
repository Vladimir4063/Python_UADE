
midiccionario = {"Alemania": "Berlín", "Francia": "Paris",
                 "Reino Unido": "Londres", "España": "Madrid"}

print(midiccionario["Francia"])  # Imprime su capital

print(midiccionario)  # Print to dictionary

midiccionario["Alemania"] = "Bs As"  # Modifique un elemento
print(midiccionario)

midiccionario["Alemania"] = "Berlín"  # Reasigne
print(midiccionario)

del midiccionario["Francia"]  # Delete a keyword
print(midiccionario)

#

diccionario1 = {"Alemania": "Berlin", 23: "Jordan"}  # Puede guardar enteros

mitupla = ["España", "Francia", "Reino Unido", "Alemania"]
midiccionario2 = {mitupla[0]: "Madrid", mitupla[1]: "Paris", mitupla[2]    : "Londres", mitupla[3]: "Berlin"}  # Agregue valores a la tupla
print(midiccionario2)

print("__________________________")

dictionary = {23: "Jordan", "Nombre": "Michael", "Equipo": "Chicago",
              "Anillos": [1991, 1992, 1993, 1996, 1997, 1998]}

print(dictionary["Nombre"])

print(dictionary.keys())  # imprime solo las llaves
print(dictionary.values()  # Imprime solo los valores)
print(len(dictionary))  # Cantidad de elem.
print(dictionary)
