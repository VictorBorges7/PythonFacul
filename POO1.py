class Pessoa:
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}.'

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa('Victor', 18, 'Masculino')

print(pessoa1.cumprimentar())
print(f'idade: {pessoa1.idade}')
pessoa1.aniversario()
print(f'idade após aniversario: {pessoa1.idade}')

print('======================================================')
print('Heranca em python')

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def fazerBarulho(self):
        pass
class Cachorro(Animal):
    def fazerBarulho(self):
        return "Latir"  
class Gato(Animal):
    def fazerBarulho(self):
        return "Miar"

meg = Cachorro("Meg")
Piquiru = Gato("Piquiru")

print(f'{meg.nome} faz: {meg.fazerBarulho()}')
print(f'{Piquiru.nome} faz: {Piquiru.fazerBarulho()}')

print('========================================================')
print('Exercicio mais complexo')

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento

    def frear(self, decremento):
        self.velocidade -+ decremento    

    def status(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, potencia):
        super().__init__(marca, modelo, ano)
        self.potencia = potencia
    
    def acelerar(self, incremento):
        self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def status(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Tipo: {self.tipo}, Velocidade: {self.velocidade} km/h'

carro1 = Carro("Ferrari", "F40", 2006, 150)
Bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

carro1.acelerar(50)
Bicicleta1.acelerar(20)

print('Status do carro:')
print(carro1.status())

print('\n Status da bike: ')
print(Bicicleta1.status())

