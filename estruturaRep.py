# Estruturas de repetição em Python

print("=== Exemplo 1: while simples ===")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # incrementa para não virar loop infinito

print("\n=== Exemplo 2: for com range ===")
# range(início, fim, passo)
for i in range(0, 10, 2):  # começa em 0, vai até 9, pulando de 2 em 2
    print("Número:", i)

print("\n=== Exemplo 3: for em lista ===")
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print("Fruta:", fruta)

print("\n=== Exemplo 4: break no while ===")
contador = 0
while True:  # loop infinito controlado pelo break
    print("Loop infinito, contador:", contador)
    if contador == 3:
        print("Saindo com break")
        break
    contador += 1

print("\n=== Exemplo 5: continue no for ===")
for i in range(6):
    if i % 2 == 0:
        continue  # pula os pares
    print("Número ímpar:", i)

print("\n=== Exemplo 6: else em laços ===")
for i in range(3):
    print("Rodando:", i)
else:
    print("Loop terminou sem break!")

print("\n=== Exemplo 7: else com break ===")
for i in range(5):
    print("Rodando:", i)
    if i == 2:
        print("Break acionado!")
        break
else:
    print("Este else não será executado")

print("\n=== Exemplo 8: loop aninhado ===")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

print("\n=== Exemplo 9: while com continue ===")
contador = 0
while contador < 6:
    contador += 1
    if contador == 3:
        print("Pulando o número 3")
        continue
    print("Número:", contador)
