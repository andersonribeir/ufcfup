def lermatriz(matriz):
	arquivo = open(matriz,"r")
	listamatriz = arquivo.readlines()

	return listamatriz

def separarmatriz(matriz):
	matrizfinal = []
	for i in range(0,len(matriz)):
		matrizfinal.append(matriz[i].strip().split(","))
	
	return matrizfinal


def multmatriz(matriz1,matriz2):
	matriz3 = [[0,0,0],[0,0,0],[0,0,0]]

	for i in range(3):
		for j in range(3):
			mult = 0
			for k in range(3):
				mult = mult + (int(matrizsep[i][k]) * int(matrizsep2[k][j]))
				matriz3[i][j]= mult
	return matriz3


def gravamatriz(matriz):
	arquivo = open("matriz3.txt","w")
	for i in range(3):
		arquivo.write(str(matriz[i]).strip("[]")+"\n")


matriz1 = lermatriz("matriz1.txt")
matrizsep = separarmatriz(matriz1)

matriz2 = lermatriz("matriz2.txt")
matrizsep2 = separarmatriz(matriz2)

multmatriz = multmatriz(matrizsep,matrizsep2)
gravamatriz(multmatriz)




		

		





