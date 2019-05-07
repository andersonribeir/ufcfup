cod_poduto = [0]*10
total_estoque = [0]*10

for i in range(0,10):
	prod = input("Entre com o código do %dº produto: "%(i+1))
	est = int(input("Entre com o total de produtos: "))
	cod_poduto[i] = prod
	total_estoque[i] = est
while True:
	cod_cliente = input("Entre com o código do cliente: ")
	cod_poduto_entrada = input("Entre com o código do produto: ")
	qtd = int(input("Entre com a quantidade de produtos: "))

	for i in range(0,len(cod_poduto+1)):
		if cod_poduto_entrada == cod_poduto[i]:
			if qtd <= total_estoque[i]:
				total_estoque[i] = total_estoque[i] - qtd
			else:
				print("A quantidade em estoque é menor")

			