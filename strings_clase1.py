vocales = "aeiou"
contador = 0
texto = "Hola Mundo"
for i in range(0,len(texto)):
    for f in range(0,5):
        if(texto[i] == vocales[f]):
            contador = contador + 1
            
print(texto[5:])

variable1 = "5"
variable2 = 4
variable3 = "10.5"
print(type(variable1))
print(type(variable2))
print(int(variable1) + 10) # CAST
print(float(variable3))

textoNvo = "Apto para instalaciones electricas"
textocsv = "10|Juan|Perez|40001001|7"
lstTexto = textoNvo.split("t")
alumno = textocsv.split("|")
print(lstTexto)
print(alumno)
print("Legajo: ", int(alumno[0]) * 100)
print("Alumno: ", alumno[1])
print(textocsv)
print(alumno)
print("||".join(alumno))

print(textoNvo.upper())
minusculas = textoNvo.lower()
print(minusculas)
print(textoNvo.replace("a", "@").replace("0", "O"))
print(textocsv.replace("|", ",").replace("Juan", "Carlos"))

print("Legajo | Nombre          |DNI       |Materias Aprobadas")
print("{0} | {1} | {2} | {3}"(alumno[0], alumno[1], alumno[2], alumno[3]))