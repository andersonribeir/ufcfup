mat = [[0,0,0],[0,0,0],[0,0,0]]


i = 0

while True:#EU SEI QUE DAVA PRA FAZER ISSO AQUI POR FOR
	#LINHA 1
	if mat[0][0]==mat[0][1] and mat[0][1]==mat[0][2] and mat[0][2]==1 :
		print ("O JOGADOR 1 VENCEU")
		break
	elif mat[0][0]==mat[0][1] and mat[0][1]==mat[0][2] and mat[0][2]==2 :
		print ("O JOGADOR 2 VENCEU")
		break
	#LINHA 2
	elif mat[1][0]==mat[1][1] and mat[1][1]==mat[1][2] and mat[1][2]==1 :
		print ("O JOGADOR 1 VENCEU")
		break
	elif mat[1][0]==mat[1][1] and mat[1][1]==mat[1][2] and mat[1][2]==2 :
		print ("O JOGADOR 2 VENCEU")
		break
	#LINHA 3
	elif mat[2][0]==mat[2][1] and mat[2][1]==mat[2][2] and mat[2][2]==1 :
		print ("O JOGADOR 1 VENCEU")
		break
	elif mat[2][0]==mat[2][1] and mat[2][1]==mat[2][2] and mat[2][2]==2 :
		print ("O JOGADOR 2 VENCEU")
		break
	#DIAGONAL DIREITA
	elif mat[0][0]==mat[1][1] and mat[1][1]==mat[2][2] and mat[2][2]==1 :
		print ("O JOGADOR 1 VENCEU")
		break
	elif mat[0][0]==mat[1][1] and mat[1][1]==mat[2][2] and mat[2][2]==2 :
		print ("O JOGADOR 2 VENCEU")
		break
	#DIAGONAL ESQUERDA
	elif mat[0][2]==mat[1][1] and mat[1][1]==mat[2][0] and mat[2][0]==1 :
		print ("O JOGADOR 1 VENCEU")
		break
	elif mat[0][2]==mat[1][1] and mat[1][1]==mat[2][0] and mat[2][0]==2 :
		print ("O JOGADOR 2 VENCEU")
		break		
	#COLUNA 1
	elif mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[2][0] ==1:
		print("O JOGADOR 1 VENCEU")
		break
	elif mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0] and mat[2][0] ==2:
		print("O JOGADOR 2 VENCEU")
		break

	#COLUNA 2
	elif mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[2][1] == 1:
		print("O JOGADOR 1 VENCEU")
		break
	elif mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1] and mat[2][1] == 2:
		print("O JOGADOR 2 VENCEU")
		break

	#COLUNA 3
	elif mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[2][2] == 1:
		print("O JOGADOR 1 VENCEU")
		break
	elif mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2] and mat[2][2] == 2:
		print("o JOGADOR 2 VENCEU")
		break

	elif mat[0][0] != 0 and mat[0][1] != 0 and mat[0][2] != 0 and mat[1][0] != 0 and mat[1][1] != 0 and mat[1][2] != 0 and mat[2][0] != 0 and mat[2][1] != 0 and mat[2][2] != 0:
		print("EMPATE")
		break

	else:
		if i%2 == 0:
			jogadalinha = int(input("JOGADOR 1 - Entre com o valor da linha: "))
			jogadacoluna = int(input("JOGADOR 1 - Entre com valor da coluna: "))
			if mat[jogadalinha-1][jogadacoluna-1] == 0 :
				mat[jogadalinha-1][jogadacoluna-1] = 1
				i+=1
				for n in range(3):
					print(mat[n])

			else:	
				while mat[jogadalinha-1][jogadacoluna-1] != 0:
					print("Essa posição já está ocupada")
					jogadalinha = int(input("JOGADOR 1 - Entre com o valor da linha: "))
					jogadacoluna = int(input("JOGADOR 1 - Entre com valor da coluna: "))
					if mat[jogadalinha-1][jogadacoluna-1] == 0 :
						mat[jogadalinha-1][jogadacoluna-1] = 1
						i+=1
						for n in range(3):
							print(mat[n])
		elif i%2 !=0:
			jogadalinha = int(input("JOGADOR 2 - Entre com o valor da linha: "))
			jogadacoluna = int(input("JOGADOR 2 - Entre com valor da coluna: "))
			if mat[jogadalinha-1][jogadacoluna-1] == 0 :
				mat[jogadalinha-1][jogadacoluna-1] = 2
				i+=1
				for n in range(3):
					print(mat[n])

			else:	
				while mat[jogadalinha-1][jogadacoluna-1] != 0:
					print("Essa posição já está ocupada")
					jogadalinha = int(input("JOGADOR 2 - Entre com o valor da linha: "))
					jogadacoluna = int(input("JOGADOR 2 - Entre com valor da coluna: "))
					if mat[jogadalinha-1][jogadacoluna-1] == 0 :
						mat[jogadalinha-1][jogadacoluna-1] = 2
						i+=1
						for n in range(3):
							print(mat[n])
		
	
		

	


		  		