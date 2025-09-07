# -----------------------------
# 1. Função básica
# -----------------------------
def saudacao():
    print("Olá! Bem-vindo ao mundo das funções em Python.")

saudacao()  # Chamando a função

# -----------------------------
# 2. Função com parâmetros
# -----------------------------
def saudacao_pessoa(nome, idade):
    print(f"Olá {nome}, você tem {idade} anos!")

saudacao_pessoa("Victor", 19)

# -----------------------------
# 3. Função com retorno
# -----------------------------
def soma(a, b):
    return a + b

resultado = soma(5, 3)
print("Soma:", resultado)

# -----------------------------
# 4. Parâmetros padrão
# -----------------------------
def saudacao_idade(nome="Amigo", idade=0):
    print(f"Olá {nome}, sua idade é {idade}.")

saudacao_idade()               # Usa os valores padrão
saudacao_idade("Ana", 25)      # Sobrescreve os valores padrão

# -----------------------------
# 5. Argumentos arbitrários (*args e **kwargs)
# -----------------------------
# *args → recebe uma lista de argumentos
def soma_varios(*numeros):
    total = sum(numeros)
    return total

print("Soma vários:", soma_varios(1, 2, 3, 4, 5))

# **kwargs → recebe argumentos nomeados arbitrários
def mostrar_informacoes(**infos):
    for chave, valor in infos.items():
        print(f"{chave}: {valor}")

mostrar_informacoes(nome="Victor", idade=19, cidade="MG")

# -----------------------------
# 6. Função com docstring
# -----------------------------
def multiplicar(a, b):
    """
    Multiplica dois números e retorna o resultado.
    
    Parâmetros:
    a (int/float): Primeiro número
    b (int/float): Segundo número
    
    Retorna:
    int/float: Resultado da multiplicação
    """
    return a * b

print("Multiplicação:", multiplicar(4, 5))
help(multiplicar)  # Mostra a docstring da função

# -----------------------------
# 7. Função lambda (anônima)
# -----------------------------
quadrado = lambda x: x ** 2
print("Quadrado de 6:", quadrado(6))

# -----------------------------
# 8. Escopo de variáveis
# -----------------------------
x = 10  # Variável global

def escopo():
    x = 5  # Variável local
    print("Variável dentro da função:", x)

escopo()
print("Variável fora da função:", x)

# -----------------------------
# 9. Função dentro de função
# -----------------------------
def saudacao_com_interna(nome):
    def mensagem_interna():
        return "Bem-vindo!"
    
    return f"{mensagem_interna()} {nome}"

print(saudacao_com_interna("Victor"))

# -----------------------------
# 10. Função recursiva
# -----------------------------
def fatorial(n):
    """Calcula o fatorial de n usando recursão"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

print("Fatorial de 5:", fatorial(5))

# -----------------------------
# 11. Função como argumento
# -----------------------------
def aplicar_funcao(func, valor):
    return func(valor)

print("Aplicando lambda:", aplicar_funcao(lambda x: x**3, 3))
