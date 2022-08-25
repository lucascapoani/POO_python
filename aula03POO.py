"""
    Crie uma classe chamada Caneta com os seguintes atributos:
        - marca
        - cor
        - tipo_ponta
        - tampada
    o atributo marca deve ser do tipo string.
        Exemplos: "BIC", "FABER CASTEL", "UNI BALL"
    o atributo cor deve ser do tipo string.
        Exemplos: "Azul", "Preta", "Vermelha"
    o atributo tipo_ponta deve ser um valor real.
        Exemplos: 0.7, 0.5, 0.3)
    o atributo tampada dever um boleano. (True, False)
        -> O padrão de instância é True

    Crie os métodos para:
        - escrever
        - tampar
        - destampar
        - dados_caneta
            -> Este método deverá retornar uma string com os atributos
                do objeto

    Crie uma lista para armazenar as suas canetas.
    Crie as seguintes funções:
        - adicionar_canetas_na_lista
        - listar_todas_canetas
        - escolher_caneta.
            -> Esta função deverá retornar uma caneta escolhida da lista.
        - colocar_caneta_lixo   (retirar da lista)

"""

# ============ PRIMEIRA PARTE DO ENUNCIADO ==============

class Caneta:
    def __init__(self, marca, cor, tipo_ponta): #(atributo, atributo, atributo)
        self.marca = marca
        self.cor = cor
        self.tipo_ponta = tipo_ponta
        self.tampada = True


# =========== SEGUNDA PARTE DO ENUNCIADO ===============
    def escrever(self, texto):
        print("ESTOU ESCREVENDO.....")
        print(texto)

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def dados_caneta(self):
        return f"Marca: {self.marca} - {self.cor} - {self.tipo_ponta} - {self.tampada}"

#marca = input("Digite a marca: ") ou
'''caneta1 = Caneta(input("Digite a marca: "), "Azul", 0.7)
caneta2 = Caneta("FABER CASTEL", "Preta", 0.5)
caneta3 = Caneta(input("Digite a marca: "), "Vermelha", 0.3)

caneta1.escrever(input("Digite ALGO: "))'''

# ============== TERCEIRA PARTE DO ENUNCIADO ================

lista = []

def adicionar_caneta(nova_caneta):
    lista.append(nova_caneta)

def listar_canetas():
    for pos, caneta in enumerate(lista):
        print(pos, caneta.dados_caneta())

def escolher_caneta():
    listar_canetas()
    escolha = int(input("Escolha: "))
    return lista[escolha]

def remover_caneta(caneta):
    for c in lista:
        if c == caneta:
            lista.remove()


caneta1 = Caneta("BIC", "PRETA", 0.7)
caneta2 = Caneta("BIC", "VERMELHA", 0.3)
caneta3 = Caneta("FABER CASTELL", "AMARELA", 0.3)

caneta1.destampar()

adicionar_caneta(caneta1)
adicionar_caneta(caneta2)
adicionar_caneta(caneta3)

print(escolher_caneta().dados_caneta())

print(caneta1.dados_caneta())


