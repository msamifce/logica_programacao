# funcoes.py

def adicionar_aluno(turma, nome, idade):
    """
    Adiciona um novo aluno ao dicionário chamado turma.
    A chave é o nome do aluno e o valor é a idade.
    """
    turma[nome] = idade
    print(f"Aluno '{nome}' adicionado com sucesso!")

def listar_alunos(turma):
    """
    Exibe todos os alunos cadastrados no dicionário da turma.
    """
    if not turma:
        print("Nenhum aluno cadastrado.")
    else:
        print("--- Lista de Alunos ---")
        for nome, idade in turma.items():
            print(f"Nome: {nome:<15} Idade: {idade}")
        print("-----------------------")

def remover_aluno(turma, nome):
    """
    Remove um aluno do dicionário, dado o nome.
    """
    if nome in turma:
        del turma[nome]
        print(f"Aluno '{nome}' removido com sucesso!")
    else:
        print(f"Erro: Aluno '{nome}' não encontrado.")
