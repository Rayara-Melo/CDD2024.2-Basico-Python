#RECEBA 2 NÚMEROS DO USUÁRIO E MOSTRE ELES EM ORDEM CRESCENTE.

n1 = int(input("Digite dois números: "))
n2 = int(input("Digite mais um número: "))
if n1 > n2:
    print(f"A ordem crecesnte dos números digidos são {n2}, {n1}")
else:
    print(f"A ordem decrecesnte dos números digidos são {n1}, {n2}")