# Esto es una tupla
milista = ("Juan", 12, 1, 1997, 12, 12)

miTupla = tuple(milista)
print("Juan" in miTupla)  # Busca en la tupla

print(miTupla.count(12))  # Search element, si encuentra, cuenta e imprime.

print(len(miTupla))  # Indica cantidad de elementos en la tupla


##########################################################

mitupla2 = ("Juan", 13, 1, 1995)
nombre, dia, mes, anio = mitupla2

# Desempaquetado de tuplas

print(nombre)
print(dia)
print(mes)
print(anio)
