from livro import Livro # importando a classe livro do arquivo livro.py
import matplotlib.pyplot as plt # importando a biblioteca do matplotlib

biblioteca = [] # instanciando a lista vazia de livros

def cadastrar_livro(): # funcao para realizar o cadastro dos livros
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    genero = input("Digite o gênero do livro: ")
    quantidade = int(input("Digite a quantidade disponível: "))

    novo_livro = Livro(titulo, autor, genero, quantidade) # variavel novo_livro recebe a instancia do objeto
    biblioteca.append(novo_livro) # é adicionado a lista de livros
    print(f"\nLivro '{titulo}' cadastrado com sucesso!\n") # imprime a mensagem com sucesso

def listar_livros(): # funcao para listar os livros cadastrados
    if not biblioteca:
        print("\nNenhum livro cadastrado.\n") # se nao tem nada na lista de livros cadastrados essa mensagem é exibida
        return
    
    print("\n📚 Lista de livros cadastrados:\n")
    for i, livro in enumerate(biblioteca, start=1):
        print(f"Livro {i}:")
        livro.exibir_informacoes() # aqui é exibida as informacoes dos livros
        print("------")

def buscar_livro(): # funcao para buscar o livro pelo titulo
    titulo_busca = input("Digite o título do livro que deseja buscar: ")

    for livro in biblioteca: # para cada livro na lista de livros
        if livro.titulo.lower() == titulo_busca.lower(): # verifica se há um titulo na lista igual o titulo digitado pelo usuario
            print("\n✅ Livro encontrado:\n")
            livro.exibir_informacoes() # mensagem de livro encontrado junto com as informacoes
            return
    print("\n❌ Livro não encontrado.\n") # caso nao tenha exibe a mensagem de que não foi encontrado

def gerar_grafico(): # funcao para gerar o grafico
    generos = {} # cria um dicionario para os livros
    for livro in biblioteca:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    labels = list(generos.keys())   # gêneros
    valores = list(generos.values())  # quantidade de livros

    # é criado gráfico de barras
    plt.bar(labels, valores, color="skyblue", edgecolor="black")
    plt.title("Quantidade de Livros por Gênero")
    plt.xlabel("Gêneros")
    plt.ylabel("Quantidade de Livros")
    plt.show()  

while True: # menu da aplicacao
    print("\n=== MENU BIBLIOTECA ===")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Gerar gráfico de quantidade de livros por gênero")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        gerar_grafico()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida, tente novamente.")
