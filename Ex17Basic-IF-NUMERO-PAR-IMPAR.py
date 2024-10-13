#RECEBA UM NÚMERO E DIGA SE ELE É PAR OU ÍMPAR, POSITIVO E NEGATIVO.

n = float(input("Digite um número: "))
if n % 2 == 0:
    if n >= 0:
        print("O número informado é par e positivo")
    if n < 0:
     print("O Número informado par e negativo")
if n % 2 != 0:
    if n >= 0:
      print("O Número informado impar e positivo")
    if n < 0:
     print("O Número informado impar e negativo")
print("FIM")