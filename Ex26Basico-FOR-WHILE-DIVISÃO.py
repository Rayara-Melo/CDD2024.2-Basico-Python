#FAÇA UM CODIGO PARA LER 2 VALORES E REALIZE A DIVISAO DO PRIMEIRO
#PELO SEGUNDO VALOR RECEBIDO, CASO O SEGUNDO VALOR DIGITADO, SEJA ZERO,
# SOLICITE NOVAMENTE O VALOR, INFORMANDO QUE SÓ ACEITAMOS VALORES DIFERENTES DE ZERO.

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
while valor2 == 0:
    print("Valor invalído, só aceitamos os segundos valores diferentes de zero")
    valor2 = int(input("Digite novamente o segundo valor: "))
if valor2 != 0:
    x = valor1 / valor2
    print(x)
print("FIM, OBRIGADO(A)")
