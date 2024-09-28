n=int(input("Digite a quantidade de alunos: "))
qap=qrep=qex=0
for i in range (1, n+1):
    n1=float(input(f"Digite a nota da primeira avaliação do {i}° aluno: "))
    n2=float(input(f"Digite a nota da segunda avaliação do {i}° aluno: "))
    media=(n1+n2)/2
    if media>=7:
        qap+=1
    elif media>=4:
        qex=1
    else:
        qrep+=1
print(f"Dados da turma com {n} alunos")
print(f"Temos {qap} alunos aprovados")
print(f"Temos {qex} alunos em exame final")
print(f"Temos {qrep} alunos reprovados")