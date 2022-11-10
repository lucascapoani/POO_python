lista_profissionais = []
lista_visitantes = []
lista_visitas = []

class Profissional:
    def __init__(self, nome, especialidade, sala):
        self.__nome = nome
        self.__especialidade = especialidade
        self.__sala = sala

    def get_nome(self):
        return self.__nome

    def get_especialidade(self):
        return self.__especialidade

    def get_sala(self):
        return self.__sala

class Visitante:
    def __init__(self, nome, documento):
        self.__nome = nome
        self.__documento = documento

    def get_vis_name(self):
        return self.__nome

    def get_vis_doc(self):
        return self.__documento

class Visita:
    def __init__(self, visitante, profissional, data_visita):
        self.visitante = visitante
        self.profissional = profissional
        self.data_visita = data_visita

    def __str__(self):
        return f"{self.visitante} - {self.profissional} - {self.data_visita}"

def cadastrar_profissional():
    nome = input("Nome: ")
    especialidade = input("Especialidade: ")
    sala = input("Sala: ")
    profissional = Profissional(nome, especialidade, sala)
    lista_profissionais.append(profissional)

def localizar_profissional():
    selecionar = input("Nome do profissional: ")
    x = False
    for profissional in lista_profissionais:
        if selecionar == profissional.get_nome() or selecionar == profissional.get_especialidade():
            x = True
            print(f"Nome: {profissional.get_nome()} - Especialidade: {profissional.get_especialidade()} - Sala {profissional.get_sala()}")
            pass
    if x == False:
        print("Este profissional não existe.")

def cadastrar_visitante():
    nome = input("Nome: ")
    documento = input("Documento: ")
    visitante = Visitante(nome, documento)
    lista_visitantes.append(visitante)

def registrar_visita():
    nome_visitante = input("Nome do visitante: ")
    profissional_digitado = input("Nome do profissional:")
    for visitante in lista_visitantes:
        if visitante.get_vis_name() == nome_visitante:
            for profissional in lista_profissionais:
                if profissional.get_nome() == profissional_digitado:
                    data_visita = input("Data: ")
                    visita = Visita(nome_visitante,profissional,data_visita)
                    lista_visitas.append(visita)
                else:
                    print("Profissional não encontrado.")
        else:
            print("Profissional não existe.")

def relatorio_conferencia():
    for i in lista_visitas:
        print(i)




while True:
    escolha = input("""
    ======================
    MENU
    ======================
    1- Cadastrar Profissional
    2- Localizar Profissional
    3- Cadastrar Visitante
    4- Registrar Visita
    5- Relatório de Conferência
    Escolha: """)

    if escolha == "1": cadastrar_profissional()
    if escolha == "2": localizar_profissional()
    if escolha == "3": cadastrar_visitante()
    if escolha == "4": registrar_visita()
    if escolha == "5": relatorio_conferencia()

