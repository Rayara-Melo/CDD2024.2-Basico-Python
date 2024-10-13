#FAÇA UM ALGORITMO PARA RECEBER UM NÚMERO QUALQUER
# E IMPRIMIR NA TELA SE O NUMERO É PAR OU IMPAR, POSITIVO OU NEGATIVO.

n = int(input("Digite um número: "))
if n >= 0 and n % 2 == 0:
    print("Número POSITIVO e PAR.")
elif n < 0 and n % 2 != 0:
    print("Número NEGATIVO e IMPAR.")
elif n >= 0 and n % 2 != 0:
    print("Número POSITIVO e IMPAR.")
elif n < 0 and n % 2 == 0:
    print("Número NEGATIVO e PAR.")
print()
