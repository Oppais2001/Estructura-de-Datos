import numpy
import random
def GeneraMatriz(n,m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            valor=random.randint(1,10)
            matriz[i].append(valor)
    return matriz
def imprime_matriz(matriz):
    for i in range(3):
        print("[", end=" ")
        for j in range(3):
            print(round(matriz[i][j]),end=" ")
        print("]")
#Programa Principal
Matriz1=GeneraMatriz(3,3)
imprime_matriz(Matriz1)
determinante=numpy.linalg.det(Matriz1)
print(int(determinante))
