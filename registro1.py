def cria_produto(nome,preco,qntd):
	produto = {}
	produto['cod'] = nome
	produto['valor'] = preco
	produto['qtd'] = qntd
	return produto

def mostra_total(lista):
	totalvalor = 0
	for i in range(len(lista)):
		totalvalor += (lista[i]['qtd'])*(lista[i]['valor'])
	print("\nO valor total dos produtos é: ",totalvalor)  


def mostra_produto(cod,lista):
	for i in range(len(lista)):
		if lista[i]['cod'] == cod:
			print("\nNome produto: ",lista[i]['cod'])
			print("Preço produto: ",lista[i]['valor'])
			print("Quantidade produto: ", lista[i]['qtd'])

def elimina_duplicidade(cod,lista):
	qtd = 0
	for i in range(len(lista)):
		if lista[i]['cod'] == cod:
			qtd += lista[i]['qtd']
			preco = lista[i]['valor']
			del(lista[i])
	produto = {}
	produto['cod'] = cod
	produto['valor'] = preco
	produto['qtd'] = qtd
	lista.append(produto)
				
		
			
		
			
	

produtos = []
for i in range(1,3):
	nome = input("Entre com o nome do produto %d: "%i)
	preco = float(input("Entre com o preço do produto %d: "%i))
	qntd = int(input("Entre com a quantidade desse produto %d: "%i))

	produto = cria_produto(nome,preco,qntd)

	produtos.append(produto)

codigo = input("\nEntre com o nome do produto: ")
mostra_produto(codigo,produtos)
mostra_total(produtos)



	
