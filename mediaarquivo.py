def lernotas():
	arquivo = open("media.txt","r")
	dados = arquivo.readlines()
	arquivo.close()
	return dados

def ajeitarlista(lista):
	novalista = []
	for linha in lista:
		dado = linha.split(",")
		novalista.append(dado)
	return novalista


def calcularmedia(novalista):
	listamedia = []
	for linha in novalista:
		media = (int(linha[2]) + int(linha[1]) + int(linha[0][-2::]))/3
		
		listamedia.append(round(media,2))		
	return listamedia

def gravarmedia(listamedia,lista):
	arquivo = open("mediafinal1.txt","w")
	nomes = []
	
	for linha in lista:
		nome = linha[0].split(" ")[0]
		nomes.append(nome)
	
	for i in range(len(nomes)):
		nomenota = nomes[i] + " " + str(listamedia[i]) + "\n"
		arquivo.write(nomenota)

		




dados = lernotas()
novosdados = ajeitarlista(dados)

media = calcularmedia(novosdados)
gravarmedia(media,novosdados)



