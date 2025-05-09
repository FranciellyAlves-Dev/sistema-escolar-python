import json
import os

def carregar_dados(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    else:
        return []

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def incluir(nome_arquivo, chave, dados_novos):
    lista = carregar_dados(nome_arquivo)
    for item in lista:
        if item[chave] == dados_novos[chave]:
            print("Já existe esse código!")
            return
    lista.append(dados_novos)
    salvar_dados(nome_arquivo, lista)
    print("Incluído com sucesso.")

def listar(nome_arquivo):
    lista = carregar_dados(nome_arquivo)
    if not lista:
        print("Nenhum dado encontrado.")
    else:
        for item in lista:
            print(item)

def atualizar(nome_arquivo, chave, codigo):
    lista = carregar_dados(nome_arquivo)
    for item in lista:
        if item[chave] == codigo:
            for campo in item:
                if campo != chave:
                    novo_valor = input(f"{campo} atual: {item[campo]} | Novo {campo}: ")
                    if novo_valor != "":
                        item[campo] = novo_valor
            salvar_dados(nome_arquivo, lista)
            print("Atualizado com sucesso.")
            return
    print("Registro não encontrado.")

def excluir(nome_arquivo, chave, codigo):
    lista = carregar_dados(nome_arquivo)
    nova_lista = [item for item in lista if item[chave] != codigo]
    if len(lista) == len(nova_lista):
        print("Código não encontrado.")
    else:
        salvar_dados(nome_arquivo, nova_lista)
        print("Excluído com sucesso.")

def menu_modulo(nome, arquivo, campos, chave):
    while True:
        print(f"\n--- {nome.upper()} ---")
        print("1 - Incluir")
        print("2 - Listar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("0 - Voltar")
        op = input("Escolha uma opção: ")

        if op == "1":
            dados = {}
            for campo in campos:
                entrada = input(f"{campo}: ")
                dados[campo] = int(entrada) if "codigo" in campo or "cpf" not in campo else entrada
            incluir(arquivo, chave, dados)

        elif op == "2":
            listar(arquivo)

        elif op == "3":
            codigo = int(input("Digite o código do registro a atualizar: "))
            atualizar(arquivo, chave, codigo)

        elif op == "4":
            codigo = int(input("Digite o código do registro a excluir: "))
            excluir(arquivo, chave, codigo)

        elif op == "0":
            break
        else:
            print("Opção inválida.")

def menu_principal():
    while True:
        print("\n SISTEMA ACADÊMICO ")
        print("1 - Estudantes")
        print("2 - Professores")
        print("3 - Disciplinas")
        print("4 - Turmas")
        print("5 - Matrículas")
        print("0 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            menu_modulo("Estudantes", "estudantes.txt",
                        ["codigo", "nome", "cpf"], "codigo")
        elif opcao == "2":
            menu_modulo("Professores", "professores.txt",
                        ["codigo", "nome", "cpf"], "codigo")
        elif opcao == "3":
            menu_modulo("Disciplinas", "disciplinas.txt",
                        ["codigo", "nome"], "codigo")
        elif opcao == "4":
            menu_modulo("Turmas", "turmas.txt",
                        ["codigo", "codigo_professor", "codigo_disciplina"], "codigo")
        elif opcao == "5":
            menu_modulo("Matrículas", "matriculas.txt",
                        ["codigo_turma", "codigo_estudante"], "codigo_turma")
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# Executar o programa
menu_principal()