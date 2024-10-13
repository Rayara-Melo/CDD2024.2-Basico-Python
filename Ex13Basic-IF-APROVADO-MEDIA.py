#FAÇA UM CÓDIGO QUE RECEBA AS 3 NOTAS DE UM ALUNO E VERIFIQUE SE ELE ESTÁ APROVADO OU REPROVADO.
#CONSIDERE QUE A MÉDIA PARA APROVAÇÃO É 7,0.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f"A sua média foi: {media}, APROVADO!")
else:
    print(f"A sua média foi: {media}, REPROVADO!")
