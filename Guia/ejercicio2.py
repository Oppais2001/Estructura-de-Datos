import numpy

def matrizInversa(matriz):
    matrizinversa=numpy.linalg.inv(matriz)
    return matrizinversa

def imprime_matriz(matriz):
    for i in range(3):
        print("[", end=" ")
        for j in range(3):
            print(int(matriz[i][j]),end=" ")
        print("]")
        
matriz1=[[1,0,0],
         [2,1,1],
         [0,0,1]]
print("matriz:")
imprime_matriz(matriz1)
matrizi=matrizInversa(matriz1)
print("matriz inversa:")
imprime_matriz(matrizi)
resultado = numpy.matmul(matriz1, matrizi)
print("matriz identidad:")
imprime_matriz(resultado)

