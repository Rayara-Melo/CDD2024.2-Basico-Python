#RECEBA, DO USUÁRIO, UM NÚMERO DE 1 A 12 E MOSTRE O NOME DO MÊS
# CORRESPONDENTE. CASO O MÊS NÃO EXISTA, MOSTRAR “VALOR INVÁLIDO”.
##OBS: USANDO IF/ELIF/ELSE

repetir = "S"
while repetir == "S" or repetir == "s":
    mes = int(input("Digite o número correspondente ao um mês: "))
    if mes == 1:
        print("O mês é Janeiro")
    elif mes == 2:
        print("O mês é Fevereiro")
    elif mes == 3:
        print("O mês é Março")
    elif mes == 3:
        print("O mês é Março")
    elif mes == 4:
        print("O mês é Abril")
    elif mes == 5:
        print("O mês é Maio")
    elif mes == 6:
        print("O mês é Junho")
    elif mes == 7:
        print("O mês é Julho")
    elif mes == 8:
        print("O mês é Agosto")
    elif mes == 9:
        print("O mês é Setembro")
    elif mes == 10:
        print("O mês é Outubro")
    elif mes == 11:
        print("O mês é Novembro")
    elif mes == 12:
        print("O mês é Dezembro")
    else:
     print("Número correspondente invalído")
    repetir = input("Gostaria de tentar novamente, digite S para SIM e N PARA NÃO: ")
print("FIM")
