# Crie uma classe Porta, com os atributos:
#   - cor: (None: significa não pintada) ou
#           "VERMELHA", "BRANCA", "AMARELA"
#
#   - altura: (210: altura padrão em centímetros)
#   - largura: (60, ou 70, ou 80, ou 90 cm )
#   - aberta: (False: se porta fechada - True: se porta aberta).
#   observação: Todos atributos devem ser privados
#
#   .
# Faça os métodos:
#   - construtor, passando a largura desejada
#                   e altura como default em 210.
#   - pintar (parâmetro é uma nova cor)
#   - abrir_porta
#   - fechar_porta
#   - __str__: (mostrar todos atributos)
#
#   - crie um método privado 'tipo_pintura' que retorne
#       "SEM COR", caso a porta não esteja pintada
#       ou retorne a cor atual
#   - crie um método privado 'aberta_fechada' que retorne
#       "ABERTA" ou "FECHADA", conforme True ou False
#   - altere o __str__ para chamar esses métodos.

class Porta:
    def __init__(self, largura, altura=210):
        self.__cor = None
        self.__altura = altura
        self.__largura = self.__escolha_largura()
        self.__aberta = True

    def __escolha_largura(self):
        lst_largura = [0, 60, 70, 80, 90, 100]
        while True:
            print("---- ESCOLHA UMA OPÇÃO ----")
            escolha = input("""
            1- 60cm
            2- 70cm
            3- 80cm
            4- 90cm
            5- 100cm: """)

            if 0 < int(escolha) <= 5:
                return lst_largura[int(escolha)]
            print("ERRO.")

    def __aberta_fechada(self):
        if self.__aberta:
            return "ABERTA"
        return "FECHADA"

    def __tipo_pintura(self):
        if self.__cor == None:
            return "SEM COR"
        return self.__cor

    def pintar(self,nova_cor):
        self.__cor = nova_cor

    def abrir(self):
        self.__aberta = True

    def fechar(self):
        self.__aberta = False

    def __str__(self):
        return f"""
        ==============
        Cor: {self.__tipo_pintura()} {self.__altura} x {self.__largura} Aberta: {self.__aberta_fechada()}
        """

    '''
    ==================== MESMA COISA DE OUTRA MANEIRA ======================
    def mostra_dados(self):
        return f"""
        ==============
        Cor: {self.__cor} {self.__altura} x {self.__largura} Aberta: {self.__aberta}
        """
    '''

    '''
    ==================== MESMA COISA DE OUTRA MANEIRA 2 ======================
    def mostra_dados(self):
        print (f"""
        ==============
        Cor: {self.__cor} {self.__altura} x {self.__largura} Aberta: {self.__aberta})
        """
        
    p1.mostra_dados()
    '''



p1 = Porta(60, 200)
p2 = Porta(80)

p1.pintar("AZUL")
p1.fechar()

# print(p1.mostra_dados())

print(p1)
print(p2)


# Crie uma classe Fechadura com os atributos privados:
#   -segredo: (string)
#   -trancada: (Boleano) default = False
#       True - CHAVEADA   False - DESCHAVEADA
#
# crie os seguintes métodos:
#   -__init__ com parâmetro chave.
#       O atributo trancada sempre em False
#
#   -chavear
#   -deschavear
#
#   -chaveada_deschaveada: retorna "CHAVEADA" ou
#       "DESCHAVEADA" conforme True ou False
#       obs. este método deve ser privado.
#   -__str__: retorne chaveada_deschaveada
#   -crie um método privado para validar a chave.

class Fechadura:
    def __init__(self, segredo, trancada, chave):
        self.__segredo = None
        self.__trancada = False
        self.chave = chave

    def


