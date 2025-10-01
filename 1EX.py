

import array as arr # importando a biblioteca de array

def media(notas):
    media = sum(notas) / len(notas)   # funcao para definir a media das notas
    return media

numeroDeNotas = int(input('Quantas notas serão inseridas? ')) # variavel para guardar o numero de notas que vao ser inseridas

vetor = arr.array('f', []) # criacao do array de floats que vão receber as notas

for i in range(numeroDeNotas): # para cada nota no array armazene o valor no variavel notas e dps adicione no array
    notas = float(input(f'Digite a nota correspondente a materia {i+1}: '))
    vetor.append(notas); 

resultadoMedias = media(vetor); # chamando a funcao media para calcular a media das notas inseridas pelo usuario

situacao = 'Aprovado' if resultadoMedias >= 7 else 'Reprovado' # verifica pela média se o aluno vai ser aprovado ou não;

print('====Relatório====') # impressão do relatório
print("Notas inseridas:", list(vetor))
print(f"Média final: {resultadoMedias:.2f}")
print("Situação do aluno:", situacao)