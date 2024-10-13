#ESCREVA UM CODIGO PARA LER AS NOTAS DA 1AV E 2AV DE UM ALUNO.
#CALCULE E IMPRIMA A MEDIA DESSE ALUNO. SÓ DEVEM SER ACEITOS VALORES VÁLIDOS,
#DURANTE A LEITURA, (0 A 10) CADA NOTA
# PERGUNTA AO USUARIO SE DEJA EXERCUTAR NOVAMENTE

while True:
    nota1 = float(input("digite a primeira nota: "))
    while nota1 < 0 or nota1 > 10:
        print("nota invalida")
        nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    while nota2 < 0 or nota2 > 10:
            print("nota invalida")
            nota2 = float(input("digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    print(f" A média do aluno foi: {media}")
    resposta = int(input("1 para sim e 2 para não: "))
    if resposta == 2:
        print("Fim")
        break