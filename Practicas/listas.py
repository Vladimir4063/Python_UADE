def sumar():
    num1 = 23
    num2 = 22
    num3 = num1+num2
    return(num3)


print(sumar())

# Listas

listaNombres = ["Vladimir", "Ivan", "Norma", "Adelina", "Martin"]

listaNombres.insert(2, "Juan")  # Elijo donde quiero agregar elementos

listaNombres.extend(["Laura", "Lucas"])  # Agrega al final de lista

listaNombres.append("Jose")


# print(listaNombres[0:3])  # 0 incluye, 3 excluye..

# print(listaNombres[2:])

listaNombres.remove("Vladimir")

# Elimina al ultimo de la lista
listaNombres.pop()

print(listaNombres[:])

# Buscador de listas

print("Vladimir" in listaNombres)
