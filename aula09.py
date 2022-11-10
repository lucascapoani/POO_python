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

# CONTINUAÇÃO
# Altere o programa anterior para:
# Colocar os atributos como privados.
# Crie uma função para verificar se o aluno já está
#   matriculado.
# Crie uma classe Disciplina com os seguintes atributos
#   privados: nome_disciplina e semestre.
# Crie mais um atributo para o aluno:
#   disciplinas_em_curso, este será uma lista com as
#   disciplinas que o aluno está cursando.
#
# Crie o menu a baixo para tornar o programa funcional.
# MENU
# 1- Cadastrar aluno
# 2- Cadastrar disciplina
# 3- Escolher displinas para o aluno
# 4- Mostrar os alunos e suas disciplina em curso.


class Aluno:
    def __init__(self, nome, matricula, data):
        self.__nome = nome
        self.__matricula = matricula
        self.__data = data
        self.__disciplinas_em_curso = []

    def get_nome(self):
        return self.__nome

    def __str__(self):
        return f"Nome: {self.__nome} - {self.__matricula} {self.__data}"

class Disciplina:
    def __init__(self):
        self.__nome = self.ler_nome_disciplina()
        self.__semestre = self.ler_semestre()

    def ler_nome_disciplina(self):
        return input("Digite o nome da disciplina: ")

    def ler_semestre(self):
        while True:
            try:
                 return int(input("Digite o semestre: "))
            except:
                input("Erro. Valor informado errado. [Enter]")

def relacionar_aluno_disciplina():
    # Mostrar alunos existentes
    print(lista_alunos)
    # Selecionar um aluno
    select = input("Selecione o aluno desejado: ")
        if select in lista_alunos:

    # Mostrar disciplinas
    # Selecionar disciplinas
    # Relacionar disciplina ao aluno
    pass

def cadastrar_disciplina():
    disciplina = Disciplina()
    lista_disciplinas.append(disciplina)

def cadastrar_aluno():
    # nome = input("Nome: ")
    # matricula = input("Matricula: ")
    # data = input("Data: ")
    #
    # objAluno = Aluno(nome, matricula, data)
    # lista_alunos.append(objAluno)

    objAluno = Aluno("Ana", "111", "11/11/11")
    lista_alunos.append(objAluno)
    objAluno = Aluno("Pedro", "222", "22/11/11")
    lista_alunos.append(objAluno)
    objAluno = Aluno("Juca", "333", "33/11/11")
    lista_alunos.append(objAluno)


def menu():
    while True:
        escolha = input(
            """
            # MENU
            # 1- Cadastrar aluno
            # 2- Cadastrar disciplina
            # 3- Escolher displinas para o aluno
            # 4- Mostrar os alunos e suas disciplina em curso.
            escolha: """
        )
        if escolha == "1":
            cadastrar_aluno()

        if escolha == "2":
            cadastrar_disciplina()

        if escolha == "3":
            relacionar_aluno_disciplina()

        if escolha == "4":
            pass

lista_alunos = []
lista_disciplinas = []


menu()

