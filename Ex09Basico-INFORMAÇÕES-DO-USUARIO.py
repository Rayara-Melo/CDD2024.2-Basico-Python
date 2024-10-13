#FAÇA UM PROGRAMA PARA LER O NOME DE UMA PESSOA,
#A SUA IDADE E O SEU SALÁRIO E MOSTRE ESSAS INFORMAÇÕES NA TELA.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
print(f"Olá, {nome}, voçê está com {idade} anos e atualmente seu salário é {salario:.3f}")