#ESCREVA UM ALGORITMO QUE LEIA O NÚMERO DE LITROS VENDIDOS
#E O TIPO DE COMBUSTÍVEL (CODIFICADO DA SEGUINTE FORMA: E-ETANOL, G-GASOLINA),
#CALCULE E IMPRIMA O VALOR A SER PAGO PELO CLIENTE SABENDO-SE
# QUE O PREÇO DO LITRO DA GASOLINA É R$5,80 E O PREÇO DO LITRO DO ETANOL É R$ 4,90.

litros = float(input("Informe a quantidade de litros abastecidos: "))
tipo = input("Informe qual foi o tipo de combustível:\n"
             " ""E"" para Etanol ou ""G"" para Gasolina: ")
if tipo == "E" or tipo == "e":
    soma = (litros * 4.90)
    print(f"O valor abstecido foi: {soma:.2f}")
if tipo == "G" or tipo == "g":
     soma = (litros * 5.80)
     print(f"O valor abstecido foi: {soma:.2f}")
else:
 print("TIPO INVALIDO, digite corretamente e novamente com a letra em MAIUSCULA!")
print("Obrigado(a)")


