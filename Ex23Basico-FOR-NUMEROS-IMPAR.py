#RECEBER UM NÚMERO DO USUÁRIO  E MOSTRAR TODOS OS NÚMEROS
#ÍMPARES DO INTERVALO DE 1 ATÉ O NÚMERO DIGITADO.


n = int(input("Digite o número: "))
for x in range(1,n+1):
    if x % 2 != 0:
     print(x)
