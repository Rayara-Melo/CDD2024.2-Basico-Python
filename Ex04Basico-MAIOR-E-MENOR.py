#CRIE UM ALGORITMO QUE RECEBA 3 NÚMEROS E INFORME QUAL O MAIOR ENTRE ELES.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digiete o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2:
    print(f"O primeiro número é maior")
elif n2 > n1:
    print(f"O segundo número é maior")
elif n3 > n2 :
    print(f"O terceiro numero é maior")
print()
