import random
a = int(input("QTD DE LINHAS: "))
b = int(input("QTD DE COLUNAS: "))

matriz = []
vetor = []
for i in range(a):
   tmp = []
   for j in range(b):
       
       tmp.append(random.randint(0,10))

   matriz.append(tmp[:])


for i in range(b):
    
    vetor.append(random.randint(0,10))

for i in range(a):
    print(matriz[i])
print(vetor)


produto = 0
for i in range(a):
    for j in range(b):
        produto += vetor[i]*matriz[i][j]

print(produto)
