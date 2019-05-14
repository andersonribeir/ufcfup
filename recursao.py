def mdc(a,b):
	if b == 0:
		return a
	else:
		return mdc(a,(a%b)) 

a = input("Entre com dois valores para calcular o mdc: ")
b= a.split()

print(mdc(int(b[0]),int(b[1])))

