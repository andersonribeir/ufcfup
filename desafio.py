from random import randint
numero = []

maior = 0
k = 1
j = 0
saltos = 0
tamanho = int(input("Entre com o tamanho da lista: "))


while len(numero)!= tamanho:
	r = randint(0,100)
	if r not in numero:
		numero.append(r)

print("\nLista original: ",numero)





while k <= len(numero):		
	for i in range(0,len(numero)-1):


		if numero[i]<numero[i+1]:
			maior = numero[i+1]
			numero[i+1] = numero[i]
			numero[i] = maior
			saltos+=1
	k += 1
print("\nA lista ordenada:",numero)
print("\nE a quantidade de saltos foi: ",saltos)




		

		

	