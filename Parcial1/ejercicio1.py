import random
import numpy as np

def CrearMatrizAleatoria():
    matriz=[]
    for i in range(4):
        matriz.append([])
        for j in range(4):
            valor=random.randint(0,10)
            matriz[i].append(valor)
    return matriz

def imprimeMatriz(matriz):
    for i in range(4):
        print("[", end=" ")
        for j in range(4):
            print(matriz[i][j], end=" ")
        print("]")
        
def SumaMatricez(matriz1,matriz2):
    matriz3=[]
    #llenamos la matriz resultado de 0
    for i in range(4):
        matriz3.append([])
        for j in range(4):
            matriz3[i].append(0)
    
    for a in range(4):
        for b in range(4):
            matriz3[a][b]=matriz1[a][b]+matriz2[a][b]
            
    return matriz3
    
            
        
#Programa Principal
matriz1=CrearMatrizAleatoria()
matriz2=CrearMatrizAleatoria()
matriz3=CrearMatrizAleatoria()
print("Matriz Aleatoria 1:")
while matriz1.linalg.det==0:
    matriz1=CrearMatrizAleatoria 
imprimeMatriz(matriz1)
print("Matriz Aleatoria 2:")
while matriz2.linalg.det==0:
    matriz2=CrearMatrizAleatoria 
imprimeMatriz(matriz2)
print("Matriz Aleatoria 3:")
imprimeMatriz(matriz3)
matriz1_al_cuadrado=np.dot(matriz1,matriz1)
print("matriz 1 al cuadrado:")
imprimeMatriz(matriz1_al_cuadrado)
matriz1_al_cubo=np.dot(matriz1_al_cuadrado,matriz1)
print("matriz 1 al cubo:")
imprimeMatriz(matriz1_al_cubo)
matriz2_inversa=np.linalg.inv(matriz2)
print("matriz 2 inversa:")
imprimeMatriz(matriz2_inversa)
matriz1_al_cubo_inversa=np.linalg.inv(matriz1_al_cubo)
print("matriz inversa de matriz 1 al cubo:")
imprimeMatriz(matriz1_al_cubo_inversa)
operacion1=np.dot(matriz1_al_cubo,matriz2_inversa)
operacion2=np.dot(operacion1,matriz3)
operacion3=SumaMatricez(operacion2,matriz1_al_cubo_inversa)
print("matriz resultado de matriz 1 al cubo por matriz inversa de 2 por matriz 3 mas matriz inversa de 1 al cubo:")
imprimeMatriz(operacion3)
