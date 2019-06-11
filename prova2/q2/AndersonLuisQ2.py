#Anderson Luis Feitosa Ribeiro  470177

def lerarquivo():
	arquivo = open("horastrabalho.txt","r") #ARQUIVOS QUE FORAM CRIADOS
	itensarquivo = arquivo.readlines()
	arquivo.close()
	return itensarquivo

def organizaritens(itens):
	listaitens = []
	for linha in itens:
		listaitens.append(linha.split("\t"))


	for i in range(0,len(listaitens)):
		for j in range(0,len(listaitens[i])):
			listaitens[i][j] = listaitens[i][j].strip()
	return listaitens

def calcularporcentagem(itens):
	listaporcentagem = []
	for i in range(0,len(itens)):
		itens[i][-1] = round((int(itens[i][-1])*100)/336,2)
		listaporcentagem.append(itens[i])
	return listaporcentagem
		
def gravararquivo(itens):
	listafinal = []
	arquivo = open("porctrabalho.txt","w") #ARQUIVO QUE FORAM CRIADOS


	arquivo.write("nº nome  porcentagem\n\n")
	for i in range(0,len(itens)):
		nome = itens[i][0]
		porcentagem = str(itens[i][-1])
		dado = str(i+1)	+" " + nome +" "+ porcentagem + "%\n"
		arquivo.write(dado)
	arquivo.close()






ler = lerarquivo()
organizar = organizaritens(ler)
calcular =calcularporcentagem(organizar)
gravar = gravararquivo(calcular)


'''
Como está no arquivo:

Antonio	45
Marcos	80
Julio	90
Andressa	80

'''
