senha = 1234
i = 1
msg = "Digite sua senha: "
while i <=3:
    num = int(input(msg))
    if num == senha:
        msg = "Login efetuado com sucesso!"
        break
    elif i <= 2  :
        msg = "Digite a senha novamente"
    else:
        msg = "Senha bloqueada"
    i+=1
print(msg)