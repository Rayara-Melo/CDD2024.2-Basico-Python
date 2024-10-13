#FAÇA UM CÓDIGO QUE RECEBA AS 3 NOTAS DE UM ALUNO E VERIFIQUE SE ELE ESTÁ
#APROVADO OU REPROVADO CONSIDERE QUE A MÉDIA PARA APROVAÇÃO É 7,0.

##OBS.: ALTERE O CÓDIGO ANTERIOR E ACRESCENTE A OPÇÃO DE ALUNO EM RECUPERAÇÃO,
##CASO SUA MÉDIA SEJA MENOR QUE 7,0 E MAIOR QUE 4,00.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print(f"Aluno APROVADO com média: {media}")
elif media >= 4 and media <7:
    print(f"Aluno em RECUPREÇÃO com média: {media}")
else:
 print(f"Aluno em REPROVADO com média: {media}")