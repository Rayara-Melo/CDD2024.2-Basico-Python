#FAÇA UM ALGORITMO QUE LEIA O VALOR DO SALÁRIO MÍNIMO,CALCULE QUANTOS
# SALÁRIOS MÍNIMOS ESSE USUÁRIO GANHA E IMPRIMA NA TELA O RESULTADO.
#(BASE PARA O SALARIO MINIMO R$ 1.293,20).

minimo = 1.29320 # OU TAMBÉM PODE SOLICITAR PARA O USUÁRIO DIGITAR
# O VALOR DO SALARIO MÍNIO ATUAL
n = float(input("Digite o valor do seu salário: "))
resultado = n / minimo
print(f"Voçê ganha {resultado:.2f} de salário mínimos.")