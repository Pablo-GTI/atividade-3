usuario_correto = "admin"
senha_correta = "1234"

while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
