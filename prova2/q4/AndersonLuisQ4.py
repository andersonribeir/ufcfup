#Anderson Luis Feitosa Ribeiro  470177

def modificarstring(string):
	stringmod = string.split()
	stringmodificada = ""
	for i in stringmod:
		stringmodificada += i

	novastring = ""
	tamanho = len(stringmodificada)-1
	while tamanho>=0:
		novastring += stringmodificada[tamanho]
		tamanho-=1
	

	return novastring


def verificapalindromo(string,novastring):
	stringmod = string.split()

	stringmodificada = ""
	
	for i in stringmod:
		stringmodificada += i

	if stringmodificada == novastring:
		return 1




frase = input("Entre com uma frase: ")
novafrase = modificarstring(frase)
print("A frase original sem espaços e invertida é: %s\n"%novafrase)



verificacao = verificapalindromo(frase,novafrase)

if verificacao == 1:
	print("A frase é palindroma")
else:
	print("A frase não é palindroma")

