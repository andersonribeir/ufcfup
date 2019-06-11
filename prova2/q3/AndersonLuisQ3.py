#Anderson Luis Feitosa Ribeiro  470177

matriz1 = [[0,0],[0,0]]
matriz2 = [[0,0],[0,0]]
matriz3 = [[0,0],[0,0]]


for i in range(len(matriz1)):
	for j in range(len(matriz1[i])):
		matriz1[i][j] = int(input("Entre com a linha %d e a coluna %d da primeira matrix 2x2: "%(i,j)))

for i in range(len(matriz2)):
	for j in range(len(matriz2[i])):
		matriz2[i][j] = int(input("Entre com a linha %d e a coluna %d da segunda matrix 2x2: "%(i,j)))

for i in range(len(matriz3)):
	for j in range(len(matriz3[i])):
		if matriz1[i][j] <= matriz2[i][j]:
			matriz3[i][j] = matriz1[i][j]
		else:
			matriz3[i][j] = matriz2[i][j]
print("A matriz final é: ",matriz3)
