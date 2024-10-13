#CRIE UM ALGORITMO QUE LEIA UM NÚMERO DIFERENTE DE ZERO
#E DIGA SE ESTE NÚMERO É POSITIVO OU NEGATIVO.

n = float(input("Digite um número: "))
if n == 0:
    print("Número invalído")
elif n < 0:
    print("Número negativo")
elif n > 0:
    print("Número positivo")
print("Fim")