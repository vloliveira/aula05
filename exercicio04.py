i = 0
soma = 0

alunos = int(input("Digite quantos alunos tem na turma: "))
while i < alunos:
    nota = float(input("Digite a nota: "))
    soma+=nota
    i+=1
media = soma/alunos
print("A média da turma é: ",media)
