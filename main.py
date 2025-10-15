import xmltodict
import os
import json
import pandas as pd

# Pegar informações 
def pegar_infos(arq, valores):
    # print(f"Pegou as informações da nota {arq}")
    # with open(f"nfs/{arquivo}", 'r') as arquivo_xml:
    with open(f"nfs/{arq}", 'rb') as arquivo_xml:
        dic_arq = xmltodict.parse(arquivo_xml)
        # print(json.dumps(dic_arq, indent=4))
        try:
            
            if "NFe" in dic_arq:
                
                infos_nf = dic_arq["NFe"]["infNFe"]
            else:   
                infos_nf = dic_arq["nfeProc"]["NFe"]["infNFe"]
            
            numero_nf = infos_nf["@Id"]
            empresa_emissora = infos_nf["emit"]["xNome"]
            nome_cliente = infos_nf["dest"]["xNome"]
            end_cliente = infos_nf["dest"]["enderDest"]
            if "vol" in infos_nf["transp"]:
                peso_bruto = infos_nf["transp"]["vol"]["pesoB"]                
            else:
                peso_bruto = "Não informado na nf"

            # print(f"""
            #     Número da nf {arquivo_xml.name}: {numero_nf}
            #     Empresa Emissora: {empresa_emissora}
            #     Cliente: {nome_cliente}
            #     Endereço Cliente: {end_cliente}
            #     Peso Bruto da venda: {peso_bruto}
            #     """)
            valores.append([numero_nf, empresa_emissora, nome_cliente, end_cliente, peso_bruto])
            
            print(f"ARQUIVO LIDO COM SUCESSO: {arq}")
        except Exception as e:
            print('Erro:', e)
            print(json.dumps(dic_arq, indent=4))


colunas = ["Numero Nota", "Empresa Emissora", "Nome Cliente", "Endereço", "Peso_Bruto"]


# Pegando o nome dos arquivos
lista_arquivos = os.listdir("nfs")
# print(arquivos)

# Lista iniciada para pegar os valores das linhas
valores = []
for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)
    # Debug
    # break

# criando tabela
tabela = pd.DataFrame(columns=colunas, data=valores)

# Debug
# print(tabela)

# Criando excel
tabela.to_excel("NotasFiscais.xlsx", index=False)

    
    
    