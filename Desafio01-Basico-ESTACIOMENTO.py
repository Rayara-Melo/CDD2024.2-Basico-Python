#DADOS OS VALORES DE HORÁRIOS ABAIXO, DECIFRE A LÓGICA E FAÇA
#UM CÓDIGO PARA EXECUTAR.
# ENTRADA01 3:45
# ENTRADA02 14:20
# SAÍDA 6:05

##OBS.: Objetivo é a SAÍDA dos dados SAIR COM O HORÁRIO EM FORMATO AM.

hora1 = int(input("Digite a hora da primeira entrada: "))
minutos1 = int(input("Digite os minutos da primeira entrada: "))
hora2 = int(input("Digite a hora da segunda entrada: "))
minutos2 = int(input("Digite os minutos da segunda entrada: "))

if hora1 > 12:
    hora1 = hora1 - 12
if hora2 > 12:
    hora2 = hora2 - 12
hora = hora1 + hora2

if hora > 12:
    hora = hora - 12

min = minutos1 + minutos2
if min > 60:
    min = min - 60
    hora = hora + 1
print(f"{hora}:{min:02d}")


