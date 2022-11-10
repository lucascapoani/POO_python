# --------------------------- EXEMPLO DE GRAVAÇÃO DE UM ARQUIVO TEXTO -------------------------------- #

# ------------------ ESCREVENDO DENTRO DO ARQUIVO  ------------------- #
def abrir_arquivo_write():
    # ----------- ABERTURA DO ARQUIVO, DENTRO DA VARIÁVEL arq ------------ #
    arq = open("teste.txt", "w")
    # --------------------- DIRECIONAR O ARQUIVO ------------------------- #
    # caminho = open("/Users/ivoneimarques/Desktop/")
    # arq = open(caminho+"teste.txt","w")
    while True:
        teclado = input("\nDigite algo: ")
        if not teclado: break
        arq.write(teclado+"\n")

    # ---------------------- FECHAMENTO DO ARQUIVO ----------------------- #
    arq.close()

# ------------------ ADICIONAR NÚMERO NO TEXTO ----------------------- #
# arq.write(str(11))

# --------------------------- EXEMPLO DE LEITURA DE UM ARQUIVO TEXTO -------------------------------- #
def lendo_arquivo_read():
    arquivo = open("teste.txt", "r")
    #texto = arquivo.read()
    #print(texto)
    # ---- Pegando linha por linha ---- #
    for linha in arquivo:
        print(">>>>", linha[:-1])
        #ou print(">>>>", linha, end="")
    arquivo.close()

# --------------------------- EXEMPLO DE ABERTURA DE UM ARQUIVO COM APPEND -------------------------------- #
def abrindo_arquivo_append():
    arq = open("teste.txt", "a")
    arq.write("Nova Informacao append")
    arq.write(str(lista))
    #ou arq.write(lista.__str__())
    arq.close()

lista = ["aaa", "bbb", "ccc"]

abrir_arquivo_write()
lendo_arquivo_read()
abrindo_arquivo_append()

#texto = "Isto é apenas um teste"
#print(texto[5: 12])




