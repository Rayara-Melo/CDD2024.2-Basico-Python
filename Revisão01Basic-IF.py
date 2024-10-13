#FAÇA UM ALGORITMO QUE LEIA(receber) OS VALORES DE A,B E C E EM
# SEGUIDA IMPRIMA NA TELA A SOMA ENTRE A E B E MOSTRE SE A SOMA È MENOR QUE C.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
soma = a + b
if soma > c:
    print(f"A soma entre os valores A e B é: {soma}. Portanto, o valor de C MENOR que a soma entre A e B.")
else:
    print(f"A soma entre A e B é MENOR que o valor de C.")
