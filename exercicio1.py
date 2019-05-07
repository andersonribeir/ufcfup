num = [0]*10
totalpar = 0
totalimpar = 0
'''for i in range(0,len(num)):
	n = int(input("Entre com o valor do %dº número: "%(i+1)))
	if n%2 == 0:
		print(n,"É um número par")
		totalpar = totalpar + 1
	else:
		print(n,"É um número impar")
		totalimpar = totalimpar + 1
print("Houveram %d pares e %d impares"%(totalpar,totalimpar))'''

for i in range(0,len(num)):
	n = int(input("Entre com o valor do %dº número: "%(i+1)))
	num[i] = n
for i in range(0,len(num)):
	if num[i]%2 == 0:
		print(num[i], "É um número par")
		totalpar += 1
	else:
		print(num[i],"É um número impar")
		totalimpar += 1
print("Houveram %d pares e %d impares"%(totalpar,totalimpar))