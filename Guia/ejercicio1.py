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

matriz2=[[0,1,0,0,0],
         [0,0,3,0,5],
         [2,0,4,0,0],
         [0,0,4,1,0],
         [0,6,0,1,0]]
sc1=[0,0,0,0,0]
sc2=[0,0,0,0,0]
for i in range(5):
    for j in range(5):
        sc1[i]+=matriz1[j][i]
        sc2[i]+=matriz2[j][i]
sc1.sort()
sc2.sort()
#print(sc1)
#print(sc2)
print("matriz1:")
imprime_matriz(matriz1)
print("matriz2:")
imprime_matriz(matriz2)
print(f"valor mas alto de la suma de columnas de la matriz 1 es {sc1[-1]}")
print(f"valor mas alto de la suma de columnas de la matriz 2 es {sc2[-1]}")
msc=sc1[-1]+sc2[-1]
print(f"la suma de ambos es igual a {msc}")

sf1=[0,0,0,0,0]
sf2=[0,0,0,0,0]
for i in range(5):
    for j in range(5):
        sf1[i]+=matriz1[i][j]
        sf2[i]+=matriz2[i][j]
sf1.sort()
sf2.sort()
#print(sf1)
#print(sf2)
print(f"valor mas bajo de la suma de filas de la matriz 1 es {sf1[0]}")
print(f"valor mas bajo de la suma de filas de la matriz 2 es {sf2[0]}")
msf=sf1[0]+sf2[0]
print(f"la suma de ambos es igual a {msf}")
