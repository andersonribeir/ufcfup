#Anderson Luis Feitosa Ribeiro  470177


import random
palavras = ["aviao","mouse","cabelo","camisa","azar","flamengo","celular","teclado"]

def sortearpalavra(palavras):
	numerosorteado = random.randint(0,5)
	return palavras[numerosorteado]

def embaralharletras(palavra):
	novapalavra = ""
	for i in range(0,len(palavra)):
		novapalavra += palavra[-i+1]

	return novapalavra

def realizarjogada(palpite,palavrasorteada):
	if palpite == palavrasorteada:
		return 1
	else:
		return 0

palavrasorteada = sortearpalavra(palavras)
palavraembaralhada = embaralharletras(palavrasorteada)
	
print("A palavra sorteada foi: ",palavraembaralhada)

tentativa = 6
while True:

	
	

	if tentativa > 0:
		print("\nVocê tem %d tentativas"%tentativa)
		palpite = input("Entre com o seu palpite: ")

		jogada = realizarjogada(palpite,palavrasorteada)

		if jogada == 1:
			print("Você venceu!!!!\n")
			reset = input("Você gostaria de jogar de novo?? 'sim ou nao: ")

			if reset == "sim":
				palavrasorteada = sortearpalavra(palavras)
				palavraembaralhada = embaralharletras(palavrasorteada)
		
				print("A palavra sorteada foi: ",palavraembaralhada)

				tentativa = 6
			else:
				break

		else:
			tentativa -= 1
	else:
		print("Você perdeu!!!")
		reset = input("Você gostaria de jogar de novo?? 'sim ou nao: ")

		if reset == "sim":
			palavrasorteada = sortearpalavra(palavras)
			palavraembaralhada = embaralharletras(palavrasorteada)
	
			print("A palavra sorteada foi: ",palavraembaralhada)

			tentativa = 6
		else:
			break





	