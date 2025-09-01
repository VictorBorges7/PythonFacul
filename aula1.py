nome = input('Qual o seu nome? ')
nota1 = float(input('Digite a nota correspondente da materia numero 1: '))
nota2 = float(input('Digite a nota correspondente da materia numero 2: '))
nota3 = float(input('Digite a nota correspondente da materia numero 3: '))
nota4 = float(input('Digite a nota correspondente da materia numero 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A media do aluno {nome} é: {media:.2f}')