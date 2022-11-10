"""
Exercício utilizando arquivos textos

Utilizando 2 listas:
    lista_nomes =[]
    lista_idades =[]

crie um algoritmo que popule essas 2 listas
Salve essas listas em um arquivo chamado
    dados.txt
com o seguinte formato:
    nome;idade

exemplo de como fica o arquivo após gravação:
Pedro;23
Maria Eduarda;34
João Carlos;45
Marco;22

"""

lista_nomes = []
lista_idades = []

def popula_listas():
    while True:
        lista_nomes.append(input("Nome: "))
        if not lista_nomes[-1]:
            lista_nomes.pop()
            break
        lista_idades.append(int(input("Idade: ")))
    print(lista_nomes)
    print(lista_idades)
    input()

def grava_arquivo(nome, idade):
    try:
        arquivo = open("dados.txt", "a")
    except:
        arquivo = open("dados.txt", "w")

    arquivo.write(nome+";"+str(idade)+"\n")
    arquivo.close()

def ler_listas():
    for ind in range(len(lista_idades)):
        grava_arquivo(lista_nomes[ind], lista_idades[ind])

popula_listas()
ler_listas()






