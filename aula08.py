# Crie uma classe Aluno com os seguintes atributos:
# - nome
# - matricula
# - data_nascimento
#
# Crie uma lista com instâncias desta classe
#   - crie uma função para adicionar alunos na lista
#   - crie uma função para verificar se um aluno existe
#       ou não na lista. Esta função deve retornar os
#       dados de aluno, mas caso o aluno não conste na
#       lista, retorne a mensagem "ALUNO NÃO MATRICULADO"
#       > consulte pela matrícula ou nome
#   - crie uma função para mostrar todos os alunos da
#       lista, com nome e matricula.

class Aluno:
    def __init__(self, nome, matricula, data):
        self.nome = nome
        self.matricula = matricula
        self.data = data

# Instanciando a lista
# Instanciar = criar um objeto
# lista_alunos = [obj, obj, obj]
lista_alunos = []

def ler_dados_aluno():
    nome = input("Nome: ")
    matricula = input("Matricula: ")
    data = input("Data de Nascimento: ")
    return Aluno(nome, matricula, data)

# Criando a função para adicionar alunos na lista = função é FORA da classe, método é dentro.
def adicionar_aluno():
    lista_alunos.append(ler_dados_aluno())

def verificar_aluno_existe():
    # ler nome / matricula
    dado = input("Digite o nome ou matricula para pesquisa: ")
    # verificar se nome/matricula existe
    for aluno in lista_alunos:
        if dado == aluno.nome or dado == aluno.matricula:
            # se existir, retorna dados do aluno
            return f"Nome: {aluno.nome} - {aluno.matricula} - {aluno.data}"
    # se não existir, retorna "NAO MATRICULADO"
    return "ALUNO NÃO MATRICULADO"

def listar_alunos():
    for aluno in lista_alunos:
        print(f"Nome: {aluno.nome} - {aluno.matricula} - {aluno.data}")

def menu():
    while True:
        escolha = input("""
        MENU 
        ==================
        1 - Adicionar aluno
        2 - Verificar aluno
        3 - Lista de alunos
        Escolha: """)

        if escolha == "1":
            adicionar_aluno()
        if escolha == "2":
            print(verificar_aluno_existe())
        if escolha == "3":
            listar_alunos()

# ---- PROGRAMA PRINCIAPL ----
menu()

