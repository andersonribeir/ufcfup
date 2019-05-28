
aprovados = []
reprovados = []



arquivo = open("notas2.txt","r")

for linha in arquivo:
	lista = linha.split("\t")

	nome = lista[0]
	nota = lista[1]
	
	if float(nota) >= 7.0:
		aprovados.append(nome)
	else:
		reprovados.append(nome)		


print("os aprovados foram:")
for i in aprovados:
	print(i)
print("\nos reprovados foram:")	
for j in reprovados:
	print(j)
		
	

