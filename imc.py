peso = float(input("Entre com o seu peso: \n"))
altura = float(input("Entre com a sua altura: \n"))
imc = "%.2f" % (peso/(altura)**2)
print("Seu imc é: ", imc)

