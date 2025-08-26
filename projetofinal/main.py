# main.py
from funcoes import *

def menu_principal():
    """
    Exibe o menu principal do sistema acadêmico.
    """
    print("\n--- Menu Principal ---")
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Cadastrar Disciplina")
    print("4. Listar Disciplinas")
    print("5. Matricular Aluno")
    print("6. Lançar Nota")
    print("7. Exibir Boletim do Aluno")
    print("8. Listar Alunos por Disciplina")
    print("9. Alterar Nome de Aluno")
    print("10. Alterar Nome de Disciplina")
    print("11. Excluir Aluno")
    print("12. Excluir Disciplina")
    print("0. Sair")
    return input("Digite sua opção: ")

if __name__ == "__main__":
    while True:
        opcao = menu_principal()
        
        if opcao == '1':
            matricula = input("Digite a matrícula do aluno: ")
            nome = input("Digite o nome do aluno: ")
            adicionar_aluno(matricula, nome)
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            codigo = input("Digite o código da disciplina: ")
            nome = input("Digite o nome da disciplina: ")
            adicionar_disciplina(codigo, nome)
        elif opcao == '4':
            listar_disciplinas()
        elif opcao == '5':
            matricula = input("Digite a matrícula do aluno: ")
            codigo_disciplina = input("Digite o código da disciplina: ")
            matricular_aluno(matricula, codigo_disciplina)
        elif opcao == '6':
            matricula = input("Digite a matrícula do aluno: ")
            codigo_disciplina = input("Digite o código da disciplina: ")
            try:
                nota = float(input("Digite a nota a ser lançada: "))
                lancar_nota(matricula, codigo_disciplina, nota)
            except ValueError:
                print("Nota inválida. Por favor, digite um número.")
        elif opcao == '7':
            matricula = input("Digite a matrícula do aluno para ver o boletim: ")
            exibir_boletim(matricula)
        elif opcao == '8':
            codigo = input("Digite o código da disciplina para listar os alunos: ")
            listar_alunos_por_disciplina(codigo)
        elif opcao == '9':
            matricula = input("Digite a matrícula do aluno: ")
            novo_nome = input("Digite o novo nome do aluno: ")
            alterar_nome_aluno(matricula, novo_nome)
        elif opcao == '10':
            codigo = input("Digite o código da disciplina: ")
            novo_nome = input("Digite o novo nome da disciplina: ")
            alterar_nome_disciplina(codigo, novo_nome)
        elif opcao == '11':
            matricula = input("Digite a matrícula do aluno a ser excluído: ")
            excluir_aluno(matricula)
        elif opcao == '12':
            codigo = input("Digite o código da disciplina a ser excluída: ")
            excluir_disciplina(codigo)
        elif opcao == '0':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
