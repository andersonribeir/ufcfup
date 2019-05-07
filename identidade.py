a = int(input("Entre com a ordem da matriz: "))

matriz = []

for i in range(a):
   tmp = []
   for j in range(a):
       tmp.append(0)

   matriz.append(tmp[:])

i = 0

while i <= a-1:
    matriz[i][i] = 1
    i+=1


for i in range(i):
    print(matriz[i])


'''for i in range(a):
   vetor = [0]*a
   matriz.append(vetor)
   matriz[a][a]=1'''