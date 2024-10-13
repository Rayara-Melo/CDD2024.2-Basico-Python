#LER O NÚMERO DE ALUNOS EXISTENTES EM UMA TURMA E, APÓS ISTO,
#LER AS NOTAS DESTES ALUNOS, CALCULAR E ESCREVER A MÉDIA ARITMÉTICA
#DESSAS NOTAS LIDAS.

soma = 0
qtd = int(input("Digite o número total do alunos na turma: "))
for x in range(1,qtd+1):
    nota = float(input(f"Digite a {x} nota: "))
    soma = soma + nota
media = soma / qtd
print(f"A média da turma é {media:.2f}")
