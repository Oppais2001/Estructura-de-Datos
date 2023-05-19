import random
def filas_columnas_aleatorias():
    n=random.randint(2,5)
    m=random.randint(2,5)
    print("tenemos una matriz de: ",(n),"x",(m))
    return n,m
def creaMatriz(n,m):
    matriz1=[]
    for i in range(n):
        matriz1.append([])
        for j in range(m):
            valor=int(input("ingrese el valor de la matriz"))
            print("con i igual a: ", i+1,"con j igual a:", j+1)
            matriz1[i].append(valor)
    return matriz1
    
def imprime_matriz(n,matriz):
    for i in range(n):
        print(matriz[i])
        
def resta_matriz(n,m,m1,m2):
    matriz3=[]
    #Llenar de ceros la mtriz resultado
    for i in range(n):
        matriz3.append([])
        for j in range(m):
            matriz3[i].append(0)
    
    for a in range(n):
        for b in range(m):
            matriz3[a][b]=m1[a][b]-m2[a][b]
    return matriz3
def multiplicacion_matrices(n,m,m1,matriz1,matriz2):
    matriz3=[]
    #Llenar de ceros la mtriz resultado
    for i in range(n):
        matriz3.append([])
        for j in range(m1):
            matriz3[i].append(0)
    #multiplicacion
    for i in range(n):
        for j in range(m1):
            for k in range(m):
                matriz3[i][j]+=matriz1[i][k]*matriz2[k][j]
                print(matriz3[i][j])
    return matriz3
def ingresa_filas_columnas(m):
    n1=int(input("ingrese la cantidad de filas:"))
    m1=int(input("ingrese la cantidad de columnas:"))
    while(n1!=m):
        print("la cantidad de columnas de la matriz resultado, debeser igual a la cantidad de filas de la matriz a ingresar", end=" ")
        print(m)
        n1=m
    return m1
n,m=filas_columnas_aleatorias()
matriz1=creaMatriz(n,m)
matriz2=creaMatriz(n,m)
print("matriz1:")
imprime_matriz(n,matriz1)
print("matriz2:")
imprime_matriz(n,matriz2)
print("resta de matriz1 y matriz2:")
matriz3=resta_matriz(n,m,matriz1,matriz2)
imprime_matriz(n,matriz3)
m1=ingresa_filas_columnas(m)
matriz4=creaMatriz(n,m1)
print(m1)
print("la matriz a multiplicar sera:")
imprime_matriz(n,matriz4)
matriz5=multiplicacion_matrices(n,m,m1,matriz3,matriz4)
print("la matriz resultado sera:")
imprime_matriz(n,matriz5)


