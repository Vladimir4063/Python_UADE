import random
matriz = [[0] * 3 for i in range(0,4)]


for j in range(0,4):
    for i in range(0,3):
        matriz[j][i] = random.randint(0,50)
print(matriz)
def OrdMat(matriz):
    for i in range(0,4):
        for f in range(0,4):
            for c in range(0,3-1):
                if matriz[f][c] < matriz[f][c+1]:
                    aux = matriz[f][c+1]
                    matriz[f][c+1] = matriz[f][c]
                    matriz[f][c] = aux
                    
llama = OrdMat(matriz)
print(matriz)