arquivo = open("media.txt","r")
soma = 0
d = 0
maior = 0
menor = 100
for i in arquivo:
	if int(i) >= maior:
		maior = int(i)
	if int(i)<= menor:
		menor = int(i)



	soma+= int(i)
	d+=1
print(soma/d)
print(maior,menor)