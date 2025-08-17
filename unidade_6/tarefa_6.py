
print("=> Questão 1")
print("============")
"""
1. Crie um programa que solicite ao usuário que insira 10 palavras. Armazene essas palavras em uma lista. Depois:
  a) Exiba a lista na ordem inversa.
  b) Substitua todas as palavras que começam com a letra "a" por ***.
  c) Exiba a lista modificada.
"""

palavras = []
print("Por favor, digite 10 palavras:")


for i in range(10):  # Loop para coletar as 10 palavras (ajustado p/ 1 a 10 e não 0 a 9)
    palavra = input(f"Palavra {i+1}/10: ")
    palavras.append(palavra)

print("\nLista original:")
print(palavras)

# a) Exiba a lista na ordem inversa.
lista_inversa = palavras[::-1]  # Usamos o fatiamento de string com um passo negativo para inverter a lista.
print("\nLista na ordem inversa:")
print(lista_inversa)

# b) Substitua todas as palavras que começam com a letra "a" por "***".
for i in range(len(palavras)):
    if palavras[i].lower().startswith("a"):
        palavras[i] = "***"

# c) Exiba a lista modificada.
print("\nLista modificada (palavras que começam com 'a' substituídas):")
print(palavras)
print("------------------------------")



print("=> Questão 2") # 2. Escreva um programa que leia os nomes e as notas de 5 alunos e armazene esses dados em um dicionário
print("============")

alunos = {}
print("Por favor, digite o nome e a nota de 5 alunos.")
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ") # Só aceita texto.
    
    nota = float(input(f"Digite a nota de {nome}: ")) # Só aceita númeor inteiro/float
    alunos[nome] = nota  

# a) Exiba de maneira organizada o nome e a nota de cada aluno.
print("\nNotas dos Alunos:")
for nome_aluno, nota_aluno in alunos.items():
    print(f"Nome: {nome_aluno:<15} Nota: {nota_aluno:.2f}")

print("------------------------------")

# b) Calcule e exiba de maneira organizada a média da turma.
soma_notas = 0
for nota_aluno in alunos.values():
    soma_notas += nota_aluno

media_turma = soma_notas / len(alunos)
print(f"Média da turma: {media_turma:.2f}")

print("------------------------------")

# c) Identifique e exiba o nome do aluno de maior nota.
nome_maior_nota = ""
maior_nota = -1.0  # Usamos um float para a nota

for nome_aluno, nota_aluno in alunos.items():
    if nota_aluno > maior_nota:
        maior_nota = nota_aluno
        nome_maior_nota = nome_aluno

print(f"O aluno com a maior nota ({maior_nota:.2f}) é: {nome_maior_nota}")
print("------------------------------")



print("=> Questão 3")
print("============")

"""
A principal diferença entre essas três estruturas de dados (ou containers) reside em suas características de mutabilidade, ordenamento e forma de acesso.

LISTAS

1. Mutáveis
2. Ordenadas
3. Armazenam qualquer tipo de dado.
4. Usa-se colchete []

TUPLAS

1. Imutáveis
2. Ordenadas
3. Indexadas
4. Usa-se parenteses ()

DICIONÁRIOS

1. Mutáveis
2. Armazena-se pares de chave-valor.
3. As chaves são imutáveis
4. Ordenadas (a partir da ver 3.7)
5. Usa-se chaves {}
"""

# Exemplo de Diferenças entre Listas, Tuplas e Dicionários

# 1. LISTA
print("--- LISTAS ---")
# Listas são mutáveis (podem ser alteradas) e ordenadas.
frutas_lista = ["maçã", "banana", "laranja"]
print(f"Lista original: {frutas_lista}")

# Acessando um elemento por índice
print(f"Acessando o primeiro elemento: {frutas_lista[0]}")

# Adicionando um novo elemento
frutas_lista.append("uva")
print(f"Lista após adicionar 'uva': {frutas_lista}")

# Modificando um elemento
frutas_lista[1] = "morango"
print(f"Lista após modificar o segundo elemento: {frutas_lista}")
print("------------------------------")


# 2. TUPLA
print("\n--- TUPLAS ---")
# Tuplas são IMUTÁVEIS (não podem ser alteradas) e ordenadas.
frutas_tupla = ("maçã", "banana", "laranja")
print(f"Tupla original: {frutas_tupla}")

# Acessando um elemento por índice
print(f"Acessando o primeiro elemento: {frutas_tupla[0]}")

# TENTANDO modificar um elemento (isso irá gerar um erro!)
try:
    frutas_tupla[1] = "morango"
except TypeError as e:
    print(f"ERRO: Não é possível modificar uma tupla. {e}")
print("------------------------------")


# 3. DICIONÁRIO
print("\n--- DICIONÁRIOS ---")
# Dicionários são mutáveis (nos valores) e armazenam pares chave-valor.
pessoa = {"nome": "Ana", "idade": 25, "cidade": "São Paulo"}
print(f"Dicionário original: {pessoa}")

# Acessando um valor por sua chave
print(f"Acessando o nome: {pessoa['nome']}")

# Modificando um valor existente
pessoa["idade"] = 26
print(f"Dicionário após modificar a idade: {pessoa}")

# Adicionando um novo par chave-valor
pessoa["profissão"] = "Programadora"
print(f"Dicionário após adicionar a profissão: {pessoa}")
print("------------------------------")



print("=> Questão 4")
print("============")
"""
# 4. Elabore um programa que
# Dada a seguinte tupla de frutas:
# frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva")
# 1. Pergunte ao usuário o nome de uma fruta. Informe quantas vezes essa fruta aparece na tupla.
# 2. Se a fruta estiver presente, mostre o índice da primeira ocorrência. Caso contrário, exiba uma mensagem informando que a fruta não foi encontrada.
"""

frutas = ("banana", "maçã", "uva", "laranja", "maçã", "melancia", "uva")

fruta_procurada = input("Digite o nome da fruta que deseja procurar: ").lower()

# O comando .count() retorna quantas vezes a fruta aparece na tupla.
# A documentação de sua aula menciona o .count() para tuplas. [cite: 761, 762]
quantidade = frutas.count(fruta_procurada)
print(f"A fruta '{fruta_procurada}' aparece {quantidade} vez(es) na tupla.")

# Verifica se a fruta está presente para evitar um erro no .index()
# A aula menciona o operador 'in' para verificar a presença em listas, e o mesmo se aplica a tuplas. [cite: 611]
if fruta_procurada in frutas:
    # Se a fruta for encontrada, o .index() retorna o índice da primeira ocorrência.
    # A documentação de sua aula menciona o .index() para tuplas. [cite: 765, 766]
    primeiro_indice = frutas.index(fruta_procurada)
    print(f"O índice da primeira ocorrência de '{fruta_procurada}' é: {primeiro_indice}")
else:
    # Se a fruta não for encontrada, exibe a mensagem apropriada.
    print(f"A fruta '{fruta_procurada}' não foi encontrada na tupla.")
    
    
