import xmltodict
import os


# Pegar informações 
def pegar_infos(arq):
    # print(f"Pegou as informações da nota {arq}")
    # with open(f"nfs/{arquivo}", 'r') as arquivo_xml:
    with open(f"nfs/{arquivo}", 'rb') as arquivo_xml:
        dic_arq = xmltodict.parse(arquivo_xml)
        print(dic_arq)
        

# Pegando o nome dos arquivos
lista_arquivos = os.listdir("nfs")
# print(arquivos)

for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    # Debug
    break