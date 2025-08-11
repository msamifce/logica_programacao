import random # Módulo necessário para o Jogo de Adivinhação

# 1. Escreva um programa que imprima a tabuada (Multiplicação) de um número inteiro informado pelo usuário.
# Imprima a tabuada de maneira organizada.
print("--- Exercício 1: Tabuada ---")
try:
    numero_tabuada = int(input("Digite um número inteiro para ver a tabuada: "))
    print(f"Tabuada de {numero_tabuada}:")
    for i in range(1, 11):
        resultado = numero_tabuada * i
        print(f"{numero_tabuada} x {i} = {resultado}")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
print("-" * 30)


# 2. Escreva um programa que calcule o fatorial de um número inteiro informado pelo usuário.
print("--- Exercício 2: Fatorial ---")
try:
    numero_fatorial = int(input("Digite um número inteiro não-negativo para calcular o fatorial: "))
    if numero_fatorial < 0:
        print("Fatorial não é definido para números negativos.")
    elif numero_fatorial == 0:
        print("O fatorial de 0 é 1.")
    else:
        fatorial = 1
        for i in range(1, numero_fatorial + 1):
            fatorial *= i
        print(f"O fatorial de {numero_fatorial} é {fatorial}.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
print("-" * 30)


# 3. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números primos dessa sequência.
# A sequência será lida até que o usuário digite 'fim'.
print("--- Exercício 3: Números Primos ---")
numeros_lidos_primos = []
print("Digite uma sequência de números inteiros. Digite 'fim' para terminar.")
while True:
    entrada = input("Número (ou 'fim'): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros_lidos_primos.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("\nNúmeros primos na sequência:")
for num in numeros_lidos_primos:
    is_primo = True
    if num < 2:
        is_primo = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_primo = False
                break
    if is_primo:
        print(num)
print("-" * 30)


# 4. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima os números ímpares dessa sequência.
# A sequência será lida até que o usuário digite 'fim'.
print("--- Exercício 4: Números Ímpares ---")
numeros_lidos_impares = []
print("Digite uma sequência de números inteiros. Digite 'fim' para terminar.")
while True:
    entrada = input("Número (ou 'fim'): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros_lidos_impares.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("\nNúmeros ímpares na sequência:")
for num in numeros_lidos_impares:
    if num % 2 != 0:
        print(num)
print("-" * 30)


# 5. Escreva um programa que leia uma sequência de números inteiros informados pelo usuário e imprima a quantidade de números negativos.
# A sequência será lida até que o usuário digite 'fim'.
print("--- Exercício 5: Quantidade de Números Negativos ---")
numeros_lidos_negativos = []
print("Digite uma sequência de números inteiros. Digite 'fim' para terminar.")
while True:
    entrada = input("Número (ou 'fim'): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        numeros_lidos_negativos.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

quantidade_negativos = 0
for num in numeros_lidos_negativos:
    if num < 0:
        quantidade_negativos += 1

print(f"\nQuantidade de números negativos na sequência: {quantidade_negativos}")
print("-" * 30)


# 6. Jogo de Adivinhação
print("--- Exercício 6: Jogo de Adivinhação ---")
print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    try:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("O número é MAIOR.")
        elif palpite > numero_secreto:
            print("O número é MENOR.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
print("-" * 30)


# 7. Número de Vogais
print("--- Exercício 7: Contagem de Vogais ---")
frase = input("Digite uma frase para contar as vogais: ")

# Define as vogais para a verificação
vogais = "aeiouAEIOU"
contador_vogais = 0

# Itera sobre cada caractere da frase
for caractere in frase:
    # Verifica se o caractere está na string de vogais
    if caractere in vogais:
        contador_vogais += 1

print(f"A frase tem {contador_vogais} vogais.")
print("-" * 30)
