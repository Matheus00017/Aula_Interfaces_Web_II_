senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta")
    senha = input("Digite a senha: ")

print("Acesso liberado")
