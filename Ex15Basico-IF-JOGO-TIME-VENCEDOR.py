#LER O NOME DE 2 TIMES E O NÚMERO DE GOLS MARCADOS NA PARTIDA PARA CADA
#TIME. #ESCREVER O NOME DO VENCEDOR. CASO NÃO HAJA VENCEDOR
# DEVERÁ SER IMPRESSA A PALAVRA EMPATE.

nometime1 = input("Nome do TIME1: ")
nometime2 = input("Nome do TIME2: ")
gol1 = int(input("Quantidade de gol realizado TIME1: "))
gol2 = int(input("Quantidade de gol relizado TIME2: "))

if gol1 == gol2:
    print(f"Resultado: EMPATE")
elif gol1 > gol2:
    print(f"Resultado: O {nometime1} é Vencedor.")
else:
    print(f"Resultado:  O {nometime2} é Vencedor.")



