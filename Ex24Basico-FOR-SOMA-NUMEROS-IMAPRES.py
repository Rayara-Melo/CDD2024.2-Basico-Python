#RECEBER 10 NÚMEROS DO USUÁRIO E MOSTRE A SOMA DE TODOS OS NÚMEROS ÍMPARES.


soma = 0
for x in range(10):
    n = int(input("Digite um número: "))
    if n % 2 != 0:
     soma = soma + n
print(soma)
