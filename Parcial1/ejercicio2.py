import random
import numpy as np

def CrearMatrizAleatoria(min,max):
    matriz=[]
    for i in range(3):
        matriz.append([])
        for j in range(3):
            valor=random.randint(min,max)
            matriz[i].append(valor)
    return matriz

def imprimeMatriz(matriz):
    for i in range(3):
        print("[", end=" ")
        for j in range(3):
            print(matriz[i][j], end=" ")
        print("]")
        
def SumaMatricez(matriz1,matriz2):
    matriz3=[]
    #llenamos la matriz resultado de 0
    for i in range(3):
        matriz3.append([])
        for j in range(3):
            matriz3[i].append(0)
    
    for a in range(3):
        for b in range(3):
            matriz3[a][b]=matriz1[a][b]+matriz2[a][b]
        
    return matriz3
#Programa Principal
Matriz1=CrearMatrizAleatoria(1,10)
Matriz2=CrearMatrizAleatoria(11,30)
Matriz3=CrearMatrizAleatoria(-10,-1)
print("Matriz 1:")
imprimeMatriz(Matriz1)
print("Matriz 2:")
imprimeMatriz(Matriz2)
print("Matriz 3:")
imprimeMatriz(Matriz3)
Suma_Matriz1_Matriz2=SumaMatricez(Matriz1,Matriz2)
Matriz_Propiedad1=np.dot(Suma_Matriz1_Matriz2,Matriz3)
print("Suma de matriz 1 y matriz 3 por matriz 3:")
imprimeMatriz(Matriz_Propiedad1)
Matriz1_por_Matriz3=np.dot(Matriz1,Matriz3)
Matriz1_por_Matriz2=np.dot(Matriz2,Matriz3)
Matriz_Propiedad2=SumaMatricez(Matriz1_por_Matriz2,Matriz1_por_Matriz3)
print("Suma de matriz 1 por matriz 3 mas matriz 2 por matriz 3:")
imprimeMatriz(Matriz_Propiedad2)