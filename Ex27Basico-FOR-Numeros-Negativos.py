#LER 10 VALORES E ESCREVER DESSE VALORES LIDOS SÃO NEGATIVOS.

soma = 0
for x in range(1,10):
    n = int(input("Digite o valor: "))
    if n < 0:
        soma = soma + n
        print(f"A soma dos valores negativos é: {soma}")
print("FIM")

