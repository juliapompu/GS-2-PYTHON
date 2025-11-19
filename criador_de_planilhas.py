import csv

def ler_csv_lista_de_listas(caminho):
    dados = []
    with open(caminho, newline='', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            dados.append(linha)
    return dados

arquivo = "excel_python(Sheet1).csv"
tabela = ler_csv_lista_de_listas(arquivo)

for linha in tabela:
    print(linha)
