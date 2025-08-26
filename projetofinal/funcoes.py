# sistema_academico.py

# Dicionários que armazenarão os dados.
alunos = {}
disciplinas = {}

def adicionar_aluno(matricula, nome):
    """Adiciona um novo aluno ao dicionário `alunos`."""
    if matricula in alunos:
        print("Erro: Matrícula já existe.")
    else:
        alunos[matricula] = {
            "nome": nome,
            "disciplinas": set(),
            "notas": {}
        }
        print(f"Aluno '{nome}' com matrícula '{matricula}' cadastrado com sucesso.")

def listar_alunos():
    """Exibe a lista de todos os alunos cadastrados."""
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Lista de Alunos ---")
        for matricula, dados_aluno in alunos.items():
            print(f"Matrícula: {matricula} | Nome: {dados_aluno['nome']}")
        print("-" * 25)

def adicionar_disciplina(codigo, nome):
    """Adiciona uma nova disciplina ao dicionário `disciplinas`."""
    if codigo in disciplinas:
        print("Erro: Código da disciplina já existe.")
    else:
        disciplinas[codigo] = {
            "nome": nome,
            "alunos": set()
        }
        print(f"Disciplina '{nome}' com código '{codigo}' cadastrada com sucesso.")

def listar_disciplinas():
    """Exibe a lista de todas as disciplinas cadastradas."""
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
    else:
        print("\n--- Lista de Disciplinas ---")
        for codigo, dados_disciplina in disciplinas.items():
            print(f"Código: {codigo} | Nome: {dados_disciplina['nome']}")
        print("-" * 25)

def matricular_aluno(matricula, codigo_disciplina):
    """Matricula um aluno em uma disciplina, atualizando as estruturas de dados."""
    if matricula not in alunos:
        print(f"Erro: Aluno com matrícula '{matricula}' não encontrado.")
        return
    if codigo_disciplina not in disciplinas:
        print(f"Erro: Disciplina com código '{codigo_disciplina}' não encontrada.")
        return
    if codigo_disciplina in alunos[matricula]["disciplinas"]:
        print(f"Aviso: Aluno '{matricula}' já está matriculado em '{codigo_disciplina}'.")
    else:
        alunos[matricula]["disciplinas"].add(codigo_disciplina)
        disciplinas[codigo_disciplina]["alunos"].add(matricula)
        if codigo_disciplina not in alunos[matricula]["notas"]:
             alunos[matricula]["notas"][codigo_disciplina] = []
        print(f"Aluno '{matricula}' matriculado em '{codigo_disciplina}' com sucesso.")

def lancar_nota(matricula, codigo_disciplina, nota):
    """Lança uma nota para um aluno em uma disciplina específica."""
    if matricula not in alunos or codigo_disciplina not in alunos[matricula]["disciplinas"]:
        print(f"Erro: Aluno '{matricula}' não está matriculado na disciplina '{codigo_disciplina}'.")
        return
    
    alunos[matricula]["notas"][codigo_disciplina].append(nota)
    print(f"Nota {nota} lançada para o aluno '{matricula}' na disciplina '{codigo_disciplina}'.")

def listar_alunos_por_disciplina(codigo_disciplina):
    """Lista todos os alunos matriculados em uma disciplina."""
    if codigo_disciplina not in disciplinas:
        print(f"Erro: Disciplina com código '{codigo_disciplina}' não encontrada.")
        return
    
    lista_alunos_disc = disciplinas[codigo_disciplina]["alunos"]
    if not lista_alunos_disc:
        print(f"A disciplina '{codigo_disciplina}' não tem alunos matriculados.")
    else:
        print(f"\n--- Alunos Matriculados em '{disciplinas[codigo_disciplina]['nome']}' ---")
        for matricula_aluno in lista_alunos_disc:
            print(f"Matrícula: {matricula_aluno} | Nome: {alunos[matricula_aluno]['nome']}")
        print("-" * 25)

def exibir_boletim(matricula):
    """Exibe o boletim de um aluno, com as disciplinas, notas e status de aprovação."""
    if matricula not in alunos:
        print(f"Erro: Aluno com matrícula '{matricula}' não encontrado.")
        return
    
    dados_aluno = alunos[matricula]
    print(f"\n--- Boletim de {dados_aluno['nome']} ({matricula}) ---")
    
    total_disciplinas_aprovadas = 0
    total_medias_validas = 0
    soma_medias_aluno = 0
    
    if not dados_aluno["disciplinas"]:
        print("O aluno não está matriculado em nenhuma disciplina.")
    else:
        for codigo_disciplina in dados_aluno["disciplinas"]:
            nome_disciplina = disciplinas[codigo_disciplina]["nome"]
            notas_disciplina = dados_aluno["notas"].get(codigo_disciplina, [])
            
            if notas_disciplina:
                media_disciplina = sum(notas_disciplina) / len(notas_disciplina)
                status = "APROVADO" if media_disciplina >= 6.0 else "REPROVADO"
                print(f"Disciplina: {nome_disciplina} | Média: {media_disciplina:.2f} | Status: {status}")
                
                soma_medias_aluno += media_disciplina
                total_medias_validas += 1
                if media_disciplina >= 6.0:
                    total_disciplinas_aprovadas += 1
            else:
                print(f"Disciplina: {nome_disciplina} | Média: N/A | Status: Pendente")

    # Calcula e exibe a média geral e o status de aprovação final
    if total_medias_validas > 0:
        media_geral = soma_medias_aluno / total_medias_validas
        status_geral = "APROVADO" if total_disciplinas_aprovadas == total_medias_validas else "REPROVADO"
        print("-" * 25)
        print(f"Média Geral do Aluno: {media_geral:.2f}")
        print(f"Status Final: {status_geral}")
    else:
        print("Média geral não disponível (sem notas lançadas).")
        
    print("-" * 25)

def alterar_nome_aluno(matricula, novo_nome):
    """Altera o nome de um aluno."""
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
    else:
        alunos[matricula]['nome'] = novo_nome
        print(f"Nome do aluno com matrícula '{matricula}' alterado para '{novo_nome}'.")

def alterar_nome_disciplina(codigo, novo_nome):
    """Altera o nome de uma disciplina."""
    if codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    else:
        disciplinas[codigo]['nome'] = novo_nome
        print(f"Nome da disciplina com código '{codigo}' alterado para '{novo_nome}'.")

def excluir_aluno(matricula):
    """Exclui um aluno e remove sua matrícula das disciplinas."""
    if matricula not in alunos:
        print("Erro: Aluno não encontrado.")
    else:
        # Remove a matrícula do aluno do conjunto de alunos de cada disciplina
        for codigo_disciplina in alunos[matricula]['disciplinas']:
            disciplinas[codigo_disciplina]['alunos'].discard(matricula) # .discard() é seguro mesmo se não existir
        
        del alunos[matricula]
        print(f"Aluno com matrícula '{matricula}' removido com sucesso.")

def excluir_disciplina(codigo):
    """Exclui uma disciplina e a remove das matrículas dos alunos."""
    if codigo not in disciplinas:
        print("Erro: Disciplina não encontrada.")
    else:
        # Remove a disciplina das listas de cada aluno que a tinha
        for matricula_aluno in disciplinas[codigo]['alunos']:
            if codigo in alunos[matricula_aluno]['disciplinas']:
                alunos[matricula_aluno]['disciplinas'].discard(codigo)
                # Opcional: remover as notas da disciplina também
                if codigo in alunos[matricula_aluno]['notas']:
                    del alunos[matricula_aluno]['notas'][codigo]
        
        del disciplinas[codigo]
        print(f"Disciplina com código '{codigo}' removida com sucesso.")
