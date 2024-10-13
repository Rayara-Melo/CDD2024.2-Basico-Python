#FAÇA UM ALGORITMO QUE LEIA DOIS VALORES INTEIROS A E B, SE OS VALORES
#DE A E B FOREM IGUAIS, DEVERÁ SOMAR OS DOIS VALORES, CASO CONTRÁRIO
#DEVERÁ MULTIPLICAR # A POR B. AO FINAL DE QUALQUER UM DOS CALCULOS
#DEVE-SE ATRIBUIR O RESULTADO A UMA VARIAVEL C E IMPRIMIR O VALOR NA TELA.

conti = 1
while conti == 1:
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    if a == b:
        soma = a + b
        c = soma
        print(c)
    else:
        mult = a * b
        c = mult
        print(mult)
    conti = int(input("Gostaria de verificar novamente? Digite 1 para SIM e qualquer número para NÃO: "))
print("FIM")