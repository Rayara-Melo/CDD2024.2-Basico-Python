#ESCREVA UM ALGORITMO PARA LER 10 NÚMEROS
#E AO FINAL DA LEITURA ESCREVER A SOMA TOTAL DOS 10 NÚMEROS LIDOS.


soma = 0
for x in range(1,11,1):
    n = int(input(f"Digite um número: "))
    soma = soma + n
print(f"A soma total dos números digitados foram: {soma}")