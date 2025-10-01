class Livro:
    def __init__(self, titulo, autor, genero, quantidade): # construtor da classe livro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade
    
    def exibir_informacoes(self): # funcao que exibe as informacoes do livro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Gênero: {self.genero}")
        print(f"Quantidade disponível: {self.quantidade}")


