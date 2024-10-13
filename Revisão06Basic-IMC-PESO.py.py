#FAÇA UM ALGORITMO QUE CALCULE O IMC(INDICE DE MASSA CORPORAL) DE UMA PESSOA LEIA O SEU PESO
#PESO E SUA ALTURA E IMPRIMA NA TELA SUA CONDIÇÃO DE ACORDO COM A TABELA ABAIXO:
#FORMULA DO IMC: IMC = PESO / ALTURA²
#TABELA CONDIÇÕES IMC:
#ABAIXO DE 18.5: ABAIXO DO PESO
#ENTRE 18.6 E 24.90: PESO DE IDEAL (PARABÉNS)
#ENTRE 25.0 E 29.9: LEVEMENTE ACIMA DO PESO
#ENTRE 30.0 E 34.9: OBESIDADE GRAU I
#ENTRE 35.0 E 39.9: OBESIDADE GRAU II (SEVERA)
#MAIOR OU IGUAL A 40: OBESIDADE GRAU III (MÓRBIDA)

cont = 1
while cont !=2:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura**2)
    print()
    if imc <= 18.5:
        print(f"Seu IMC é: {imc} - ABAIXO DO PESO")
    elif imc >= 18.6 and imc <= 24.90:
            print(f"Seu IMC é: {imc} - PESO DE IDEAL (PARABÉNS)")
    elif imc >= 25 and imc <=29.9:
        print(f"Seu IMC é: {imc} - LEVEMENTE ACIMA DO PESO")
    elif imc >= 30.0 and imc <= 34.9:
        print(f"Seu IMC é: {imc} - OBESIDADE GRAU I")
    elif imc >= 35.0 and imc <= 39.9:
        print(f"Seu IMC é: {imc} - OBESIDADE GRAU II (SEVERA)")
    elif imc <= 40:
        print(f"Seu IMC é: {imc} - OBESIDADE GRAU III (MÓRBIDA)")
    cont = int(input("Gostaria de verificar novamente, digite 1 para sim e 2 para não: "))
print("FIM")