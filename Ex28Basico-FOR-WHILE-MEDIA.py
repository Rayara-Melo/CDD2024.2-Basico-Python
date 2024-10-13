#ESCREVA UM CODIGO PARA LER AS NOTAS DA 1AV E 2AV DE UM ALUNO.
#CALCULE E IMPRIMA A MEDIA DESSE ALUNO. SÓ DEVEM SER ACEITOS VALORES VÁLIDOS,
#DURANTE A LEITURA, (0 A 10) CADA NOTA
# PERGUNTA AO USUARIO SE DEJA EXERCUTAR NOVAMENTE

repetir = 1
while repetir != 2:
    soma = 0
    nota1 = float(input("Digite a primeira nota: "))
    if nota1 >= 0 or nota1 <= 10:
        soma = soma + nota1
    if nota1 < 0 or nota1 > 10:
        print("Valores invalídos. Aceitamos só os valores valídos(0-10)")
        nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    if nota2 >= 0 or nota2 <= 10:
        soma = nota1 + nota2
    if nota2 < 0 or nota2 > 10:
        print("Valores invalídos. Aceitamos só os valores valídos(0-10)")
        nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    print(f"A média foi {media}")
    repetir = float(input("Gostaria de continuar? Digite 1 para SIM e 2 para NÃO: "))
print("FIM")