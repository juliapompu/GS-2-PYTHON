import csv

import csv

def ler_csv_lista_de_listas(caminho):
    tabela = []
    with open(caminho, "r", encoding="latin-1") as f:
        linhas = f.read().splitlines()
    if len(linhas) == 1 or all((";" in linha) for linha in linhas):
        tabela = [linha.split(";") for linha in linhas]
    else:
        with open(caminho, newline='', encoding='latin-1') as f:
            leitor = csv.reader(f, delimiter=';')
            tabela = list(leitor)

    return tabela



def lista_para_dict(lista):
    cabecalho = [c.strip() for c in lista[0]]
    dados = []

    for linha in lista[1:]:
        d = {}
        for i, campo in enumerate(cabecalho):
            d[campo] = linha[i].strip()
        dados.append(d)

    return dados


def organizar_por_pais(lista_dic):
    colunas_pais_possiveis = ["Pais", "PAIS", "pais", "País", "país"]
    chave_pais = None

    for chave in colunas_pais_possiveis:
        if chave in lista_dic[0]:
            chave_pais = chave
            break

    if chave_pais is None:
        print("ERRO: Nenhuma coluna de país encontrada no CSV!")
        print("Colunas disponíveis:", list(lista_dic[0].keys()))
        exit()

    dados = {}
    for linha in lista_dic:
        pais = linha[chave_pais]
        dados[pais] = linha 
    return dados


def apresenta_dado(dados, nome_dado):
    resultado = {}
    for pais, valores in dados.items():
        if nome_dado in valores:
            try:
                resultado[pais] = float(valores[nome_dado])
            except:
                resultado[pais] = None
    return resultado


def apresenta_pais(dados, nome_pais):
    return dados.get(nome_pais, None)


def media_dado(dados, nome_dado):
    valores = [v for v in apresenta_dado(dados, nome_dado).values() if v is not None]
    return sum(valores) / len(valores)


def variancia_dado(dados, nome_dado):
    valores = [v for v in apresenta_dado(dados, nome_dado).values() if v is not None]
    m = sum(valores) / len(valores)
    return sum((v - m) ** 2 for v in valores) / len(valores)


def media_ponderada(dados, nome_dado, nome_peso):
    pares = []
    for pais, info in dados.items():
        try:
            x = float(info[nome_dado])
            w = float(info[nome_peso])
            pares.append((x, w))
        except:
            pass

    numerador = sum(x * w for x, w in pares)
    denominador = sum(w for _, w in pares)
    return numerador / denominador if denominador != 0 else None


def mediana_dado(dados, nome_dado):
    valores = sorted(v for v in apresenta_dado(dados, nome_dado).values() if v is not None)
    n = len(valores)

    if n == 0:
        return None
    if n % 2 == 1:
        return valores[n // 2]
    return (valores[n // 2 - 1] + valores[n // 2]) / 2

def menu(dados):
    while True:
        print("\n===== MENU SAFE-DADOS =====")
        print("1 - Apresentar DADO (ex: PIB, Populacao)")
        print("2 - Apresentar PAÍS (todos os dados do país)")
        print("3 - Média de um dado")
        print("4 - Variância de um dado")
        print("5 - Média ponderada")
        print("6 - Mediana de um dado")
        print("0 - Sair")

        op = input("\nEscolha uma opção: ")

        if op == "1":
            dado = input("Nome do dado: ")
            print(apresenta_dado(dados, dado))

        elif op == "2":
            pais = input("Nome do país: ")
            info = apresenta_pais(dados, pais)
            if info:
                print(info)
            else:
                print("País não encontrado!")

        elif op == "3":
            dado = input("Dado para média: ")
            valores = apresenta_dado(dados, dado).values()
            if all(v is None for v in valores):
                print("Nenhum valor numérico encontrado!")
            else:
                print("Média =", media_dado(dados, dado))

        elif op == "4":
            dado = input("Dado para variância: ")
            print("Variância =", variancia_dado(dados, dado))

        elif op == "5":
            dado = input("Dado principal: ")
            peso = input("Dado peso (ex: Populacao): ")
            print("Média Ponderada =", media_ponderada(dados, dado, peso))

        elif op == "6":
            dado = input("Dado para mediana: ")
            print("Mediana =", mediana_dado(dados, dado))

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

    while True:
        print("\n===== MENU SAFE-DADOS =====")
        print("1 - Apresentar DADO (ex: PIB, Populacao)")
        print("2 - Apresentar PAÍS (todos os dados do país)")
        print("3 - Média de um dado")
        print("4 - Variância de um dado")
        print("5 - Média ponderada (pela variável que escolher)")
        print("6 - Mediana de um dado")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        # 1 - Apresentar dado
        if opcao == "1":
            dado = input("Nome do dado: ")
            print(apresenta_dado(dados, dado))

        # 2 - Apresentar país
        elif opcao == "2":
            pais = input("Nome do país: ")
            print(apresenta_pais(dados, pais))

        # 3 - Média
        elif opcao == "3":
            dado = input("Dado para média: ")
            print("Média =", media_dado(dados, dado))

        # 4 - Variância
        elif opcao == "4":
            dado = input("Dado para variância: ")
            print("Variância =", variancia_dado(dados, dado))

        # 5 - Média ponderada
        elif opcao == "5":
            dado = input("Dado principal: ")
            peso = input("Variável de peso: ")
            print("Média ponderada =", media_ponderada(dados, dado, peso))

        # 6 - Mediana
        elif opcao == "6":
            dado = input("Dado para mediana: ")
            print("Mediana =", mediana_dado(dados, dado))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


arquivo = r"c:\Users\Pompeu\GS-2-PYTHON\excel_python.csv"

tabela = ler_csv_lista_de_listas(arquivo)
lista_dic = lista_para_dict(tabela)
dados = organizar_por_pais(lista_dic) 

menu(dados)
