# Lista de Exercícios - Tarefa 3

# 1
print("===> Questão 1 ")
num11 = float(input("Digite o primeiro número: "))
num22 = float(input("Digite o segundo número: "))

soma = num11 + num22
subtracao = num11 - num22
multiplicacao = num11 * num22
divisao = num11 / num22

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}") # Não validada se dividido por zero (Pode dar erro).

print("-" * 30) # Barra separadora 

# 2
print("===> Questão 2 ")
try:
    base_triangulo = float(input("Digite a base do triângulo: "))
    altura_triangulo = float(input("Digite a altura do triângulo: "))

    if base_triangulo > 0 and altura_triangulo > 0:
        area_triangulo = (base_triangulo * altura_triangulo) / 2
        print(f"A área do triângulo é: {area_triangulo}")
    else:
        print("A base e a altura devem ser maiores que zero.")
except ValueError:
    print("Entrada inválida. Por favor, digite números para base e altura.")
print("-" * 30)


# 3
print("===> Questão 3 ")
try:
    ganho_por_hora = float(input("Quanto você ganha por hora? R$ "))
    horas_por_dia = float(input("Quantas horas você trabalha por dia? "))

    horas_por_semana = horas_por_dia * 5
    # Considerando um mês com 4 semanas (aproximação comum para cálculo mensal)
    horas_por_mes = horas_por_semana * 4
    salario_mensal = ganho_por_hora * horas_por_mes

    print(f"Seu salário mensal estimado é: R$ {salario_mensal:.2f}") # .2f para formatar com 2 casas decimais
except ValueError:
    print("Entrada inválida. Por favor, digite números.")
print("-" * 30)


# 4
print("===> Questão 4 ")
try:
    idade_anos = int(input("Digite a sua idade em anos: "))

    # Aproximação: 365 dias por ano. Ignora anos bissextos para simplificar.
    dias_vividos = idade_anos * 365
    print(f"Você viveu aproximadamente {dias_vividos} dias.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a idade.")
print("-" * 30)


# 5
print("===> Questão 5 ")
nome_usuario = input("Digite seu nome: ")
sobrenome_usuario = input("Digite seu sobrenome: ")

nome_completo = nome_usuario + " " + sobrenome_usuario
print(f"Seu nome completo é: {nome_completo}")
print("-" * 30)


# 6
print("===> Questão 6 ")
try:
    temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit (°F): "))

    # Fórmula Fahrenheit para Celsius: C = (F - 32) * 5/9
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    # Fórmula Celsius para Kelvin: K = C + 273.15
    temp_kelvin = temp_celsius + 273.15

    print(f"Temperatura em Celsius: {temp_celsius:.2f}°C")
    print(f"Temperatura em Kelvin: {temp_kelvin:.2f}K")
except ValueError:
    print("Entrada inválida. Por favor, digite um número para a temperatura.")
print("-" * 30)


# 7
print("===> Questão 7 ")
string_numeros = input("Digite uma string de 0s e 1s (ex: 1011001): ")

# O método .count() de strings é perfeito para isso
quantidade_uns = string_numeros.count('1')

print(f"A quantidade de '1's na string é: {quantidade_uns}")
print("-" * 30)

# 8
print("===> Questão 8 ")
palavra = input("Digite uma palavra: ")

# Fatiamento de string em Python: [start:end:step]
# O passo -1 inverte a string
palavra_invertida = palavra[::-1]

print(f"A palavra invertida é: {palavra_invertida}")
print("-" * 30)

# 9
print("===> Questão 9 ")
frase_com_espacos = input("Digite uma frase com espaços: ")

# O método .replace() substitui todas as ocorrências de um caractere por outro
frase_sem_espacos = frase_com_espacos.replace(" ", "")

print(f"Frase sem espaços: {frase_sem_espacos}")
print("-" * 30)

# 10
print("===> Questão 10 ")
frase1_ex10 = input("Digite a primeira frase: ")
frase2_ex10 = input("Digite a segunda frase: ")

# Processar a primeira frase
frase1_invertida = frase1_ex10[::-1]
frase1_modificada = frase1_invertida.replace('A', '*').replace('a', '*') # Substitui 'A' e 'a'

# Processar a segunda frase
frase2_invertida = frase2_ex10[::-1]
frase2_modificada = frase2_invertida.replace('A', '*').replace('a', '*') # Substitui 'A' e 'a'

print(f"\nPrimeira frase invertida e modificada: {frase1_modificada}")
print(f"Segunda frase invertida e modificada: {frase2_modificada}")
print("-" * 30)

