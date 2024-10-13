#LER UMA VARIÁVEL DE NÚMERO INTEIRO
#E MOSTRAR A TABUADA DE MULTIPLICAÇÃO DESSE NÚMERO (1-10). FORMATO DA SAÍDA:
#1 X 5 = 5
#2 X 5 = 10 ...

n = int(input("Digite o número da tabuada que deseja realizar: "))
print(f"A tabuada do número {n} é:")
for x in range(1,11):
    mult = n * x
    print(f"{n}x{x} = {mult}")