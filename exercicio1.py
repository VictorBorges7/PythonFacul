import matplotlib.pyplot as plt

# Classe para representar um livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}"

# Criar uma lista de livros
biblioteca = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    print(f"{titulo} foi adicionado à biblioteca.")

# Função para listar todos os livros na biblioteca
def listar_livros():
    print()
    for livro in biblioteca:
        print(livro)

# Adicionar alguns livros à biblioteca
adicionar_livro("Dom Quixote", "Victor Borges", 1605)
adicionar_livro("Como ficar rico facil e rapido", "Victor Borges", 1813)
adicionar_livro("Como ser ref e cria de konoha", "Victor Borges", 1949)
adicionar_livro("Como derrotar o uchiha madara", "Victor Borges", 1967)
adicionar_livro("Como fazer um katon", "Victor Uchiha", 1951)

# Listar todos os livros na biblioteca
listar_livros()

# Criar lista com os anos de publicação
anos = [livro.ano_publicacao for livro in biblioteca]

# Remover duplicatas e ordenar
anos_unicos = sorted(set(anos))

# Contagem de livros por ano
contagem_por_ano = [anos.count(ano) for ano in anos_unicos]

# Criar um gráfico de linha
plt.plot(anos_unicos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

# Adicionar rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos_unicos[i], valor, str(valor), ha='center', va='bottom')

plt.grid(True)
plt.show()
