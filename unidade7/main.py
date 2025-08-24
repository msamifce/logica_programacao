"""Questões 1 a 4 da atividade"""

def encontrar_minimo(lista_numeros):
    """
    01. Recebe uma lista de números e retorna o valor mínimo.
    """
    if not lista_numeros:
        return None  # Retorna None para listas vazias para evitar erro

    # A maneira mais eficiente e 'pythônica' é usar a função min()
    return min(lista_numeros)

# Exemplo de uso
numeros = [5, 2, 8, 1, 9, 3]
minimo_valor = encontrar_minimo(numeros)
print(f"O valor mínimo na lista é: {minimo_valor}")

def primeiros_n_valores(lista, n):
    """
    02. Recebe uma lista e um inteiro n, e retorna uma nova lista com os n primeiros valores.
    """
    # A fatia de lista (slicing) é a forma mais simples e direta de fazer isso.
    # [0:n] significa "comece do índice 0 e vá até o índice n (não o inclua)".
    return lista[:n]

# Exemplo de uso
lista_original = [10, 20, 30, 40, 50, 60, 70]
n_valores = 4
primeiros_valores = primeiros_n_valores(lista_original, n_valores)
print(f"Os {n_valores} primeiros valores da lista são: {primeiros_valores}")

"""
03. - Vão ficar todos nesse arquivo mesmo, mas o exercício 5 está dividido em 2 arquivos.
"""
def calcular_media(lista):
    """Calcula a média de uma lista de números."""
    if not lista:
        return 0
    return sum(lista) / len(lista)

def imprimir_tabuada(numero):
    """Imprime a tabuada de multiplicação de um número."""
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def filtrar_maiores_que(lista, valor):
    """Retorna os valores de uma lista que são maiores que um valor específico."""
    maiores_valores = []
    for num in lista:
        if num > valor:
            maiores_valores.append(num)
    return maiores_valores

# import meu_modulo - Acabou ficando tudo nesse arquivo, referente as questões 1 a 4.

minha_lista = [10, 20, 30, 40, 50]

# Operação 1: Calcular a média de uma lista de números
media = meu_modulo.calcular_media(minha_lista)
print(f"A média da lista é: {media}")

# Operação 2: Imprimir a tabuada de um número
num_tabuada = int(input("\nDigite um número para ver a tabuada: "))
meu_modulo.imprimir_tabuada(num_tabuada)

# Operação 3: Filtrar valores maiores que um número
valor_filtro = int(input("\nDigite um valor para filtrar a lista: "))
lista_filtrada = meu_modulo.filtrar_maiores_que(minha_lista, valor_filtro)
print(f"Os números da lista maiores que {valor_filtro} são: {lista_filtrada}")

def analisa_lista(lista_numeros):
    """
    04. Recebe uma lista de números e retorna um dicionário com estatísticas.
    """
    if not lista_numeros:
        return {
            "soma": 0,
            "media": 0,
            "maior": None,
            "menor": None
        }

    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    maior = max(lista_numeros)
    menor = min(lista_numeros)

    resultado = {
        "soma": soma,
        "media": media,
        "maior": maior,
        "menor": menor
    }
    return resultado

# Exemplo de uso
outra_lista = [12, 5, 23, 17, 8]
estatisticas = analisa_lista(outra_lista)
print(f"Estatísticas da lista: {estatisticas}")

"""Questão 5 (CRUD) """

# main.py

# Importa todas as funções do arquivo funcoes.py
from funcoes import *

# Inicializa o dicionário vazio que será usado para armazenar os alunos
turma = {}

while True:
    print("\n--- Menu Principal ---")
    print("1: Adicionar um aluno.")
    print("2: Listar todos os alunos.")
    print("3: Remover um aluno.")
    print("4: Sair.")

    escolha = input("Digite sua opção (1-4): ")

    if escolha == '1':
        nome_aluno = input("Digite o nome do aluno: ")
        # Tenta converter a idade para um número.
        try:
            idade_aluno = int(input("Digite a idade do aluno: "))
            adicionar_aluno(turma, nome_aluno, idade_aluno)
        except ValueError:
            print("Idade inválida. Por favor, digite um número.")
    elif escolha == '2':
        listar_alunos(turma)
    elif escolha == '3':
        nome_aluno = input("Digite o nome do aluno a ser removido: ")
        remover_aluno(turma, nome_aluno)
    elif escolha == '4':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
