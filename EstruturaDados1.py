texto = "Explorando a diversidade de linguagens de programação com Pyhton."

print(f"Tamanho do texto = {len(texto)}")

print(f"Python in texto = {'Python' in texto}")

print(f"Quantidade de e no texto = {texto.count('e')}")

print(f"As 5 primeiras letras são: {texto[:5]}")
#------------------------------------------------
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']

for cor in cores:

    print(f'Posição = {cores.index(cor)}, cor = {cor}')
#-------------------------------------------------
linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]

print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("\nDepois da listcomp = ", linguagens)
#------------------------------------------------
precos_em_dolares = [100, 50, 75, 120]

taxa_de_cambio = 5.25

precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))

print(precos_em_reais)
#-------------------------------------------------
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)
# -------------------------------------------------
vogais = ('a', 'e', 'i', 'o', 'u')

print(f"Tipo do objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):

    print(f"Posição = {p}, valor = {x}")
#-------------------------------------------------

# Tupla de convidados

convidados = ("Alice", "Bob", "Carol", "David", "Eve")

# Lista de confirmações

confirmados = ["Bob", "David"]

# Identificar quem ainda não confirmou

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]

# Exibir os convidados que ainda não confirmaram

print("Convidados que ainda não confirmaram:")

for pessoa in nao_confirmados:

    print(pessoa)

# Enviar lembretes aos não confirmados

print("\nEnviando lembretes para os convidados que ainda não confirmaram.")