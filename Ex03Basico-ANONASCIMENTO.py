#CRIE UM ALGORITMO QUE LEIA A IDADE DE UMA PESSOA E DIGA
# EM QUAL ANO ELA NASCEU.

idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))
nascimento = ano_atual - idade
print(f"Seu ano de nascimento foi em {nascimento}.")


