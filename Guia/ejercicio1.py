def imprime_matriz(matriz):
    for i in range(5):
        print("[", end=" ")
        for j in range(5):
            print(matriz[i][j],end=" ")
        print("]")

matriz1=[[1,0,0,3,0],
         [2,0,1,0,0],
         [0,1,0,0,1],
         [2,0,3,0,0],
         [1,0,1,0,0]]
sc1=[0,0,0,0,0]
for i in range(5):
    for j in range(5):
        sc1[i]+=matriz1[j][i]
sc1.sort()
#print(sc1)
print("matriz1:")
imprime_matriz(matriz1)
print(f"valor mas alto de la suma de columnas de la matriz 1 es {sc1[-1]}")

sf1=[0,0,0,0,0]
for i in range(5):
    for j in range(5):
        sf1[i]+=matriz1[i][j]
sf1.sort()
#print(sf1)
print(f"valor mas bajo de la suma de filas de la matriz 1 es {sf1[0]}")

