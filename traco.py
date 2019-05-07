import random
a = int(input("Entre com a ordem da matriz: "))
matriz = []
for i in range(a):
   tmp = []
   for j in range(a):
       tmp.append(random.randint(0,10))
   
   matriz.append(tmp[:])
   print(matriz[i])

soma = 0
i = 0

while i <= a-1:
    soma += matriz[i][i]
    i+=1
    
print(soma)


