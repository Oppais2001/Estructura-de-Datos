import random

def creaMatriz(n,m):
    matriz=[]
    for i in range(n):
        matriz.append([])
        for j in range(m):
            valor=float(random.randint(1,10))
            matriz[i].append(valor)
    return matriz

def matrizinversa(matriz,matrizidentidad):
    n=len(matriz)
    #vuelve todos los primeros valores de cada fila 1
    for a in range(n):
        if matriz[a][0]!=1:
            divisor=matriz[a][0]
            for b in range(n):
                if divisor!=0 or divisor!=-0.0:
                    matriz[a][b]/=divisor
                    matrizidentidad[a][b]/=divisor
    # le resta la fila 1 a la fila 2 y a la fila 3
    for i in range(1,n):
        for j in range(n):
            matriz[i][j]-=matriz[0][j]
            matrizidentidad[i][j]-=matrizidentidad[0][j]
    #vuelve todos los segundos valores de las filas distintas a la primera 1
    for c in range(1,n):
        if matriz[c][1]!=1:
            divisor=matriz[c][1]
            for d in range(n):
                if divisor!=0 or divisor!=-0.0:
                    matriz[c][d]/=divisor
                    matrizidentidad[c][d]/=divisor
    # le resta la fila 2 a la fila 3
    for e in range(2,n):
        for f in range(n):
            matriz[e][f]-=matriz[1][f]
            matrizidentidad[e][f]-=matrizidentidad[1][f]
    #vuelve el valor de la lista m(3,3) un 1
    for g in range(2,n):
        if matriz[g][2]!=1:
            divisor=matriz[g][2]
            for h in range(n):
                if divisor!=0 or divisor!=-0.0:
                    matriz[g][h]/=divisor
                    matrizidentidad[g][h]/=divisor
    #obtenemos el indice de los valores de la columna 3
    for z in range(n-1):
        multiplicador=matriz[z][2]
        matriz[z][2]-=multiplicador*matriz[2][2]
        matrizidentidad[z][2]-=multiplicador*matrizidentidad[2][2]
        #multiplicador=matriz[z][2]
        #matriz[z][2]-=multiplicador*matriz[2][2]
        #matrizidentidad[z][2]-=multiplicador*matrizidentidad[2][2]
    multiplicador=matriz[0][1]
    matriz[0][1]-=multiplicador*matriz[1][1]
    matrizidentidad[0][1]-=multiplicador*matriz[1][1]
    return matriz,matrizidentidad

def creaMatrizIdentidad(n):
    matriz=[]
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0.0)
            if i==j:
                matriz[i][j]=1.0
    return matriz

def imprime_matriz(n,m,matriz):
    for i in range(n):
        print("[", end=" ")
        for j in range(m):
            if matriz[i][j]==-0.0:
                matriz[i][j]=0.0
            print(float(matriz[i][j]),end=" ")
        print("]")
def imprimeMatrizAmpliada(n,m,matriz):
    for i in range(n):
        print("[", end=" ")
        for j in range(m):
            if matriz[i][j]==-0.0:
                matriz[i][j]=0.0
            if j==3:
                print("|", end= "")
            print(float(matriz[i][j]),end=" ")
        print("]")

#Programa Principal
n1=3
matrizidentidad=creaMatrizIdentidad(n1)
print("matriz identidad:")
imprime_matriz(n1,n1,matrizidentidad) 
matriz1=creaMatriz(n1,n1)
print(f"crea matriz aleatoria de {n1}x{n1}")
imprime_matriz(n1,n1,matriz1)
matriz2,matrizidentidad=matrizinversa(matriz1,matrizidentidad)
for i in range(n1):
    for j in range(n1):
        matriz2[i].append(matrizidentidad[i][j])
print("matriz ampliada inversa:")
imprimeMatrizAmpliada(n1,2*n1,matriz2)