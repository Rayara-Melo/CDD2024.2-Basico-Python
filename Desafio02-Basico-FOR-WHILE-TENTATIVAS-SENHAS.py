#FAÇA UM CODIGO PARA LER A SENHA DE UM USUARIO E APÓS 3 TENTATIVAS ERRADAS
#SAIR DO PROGRAMA, INFORMANDO QUE A SENHA ESTÁ BLOQUEADA.

pin = 123
cont = 1
senha = int(input("Digite a senha: "))
while senha != pin and cont < 3:
    print("SENHA INCORRETA")
    print(f"Voçê tem mais {3-cont} tentativas!")
    senha = int(input("Digite a senha novamente: "))
    cont+=1
if cont == 3:
    print("Tentativas esgostadas. SENHA BLOQUEADA")
else:
    print("Login efetuado com sucesso!")

