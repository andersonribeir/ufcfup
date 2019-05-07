n = int(input("Entre com um número inteiro: "))

ultimo = 0
j=1
for i in range(1,n+1):
	count = 0
	for j in range(1,i+1):
		if i%j == 0:
			count += 1

	if count == 2:
		ultimo = i
print(ultimo)
