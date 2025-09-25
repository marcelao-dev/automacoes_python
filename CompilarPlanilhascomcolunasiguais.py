"""
Unificador de Planilhas Excel
Autor: Marcelo
Descrição:
    Este script busca todos os arquivos .xlsx dentro de uma pasta especificada,
    junta os dados em uma única planilha e salva o resultado em um novo arquivo.
"""

import pandas as pd
import glob
import os

# -----------------------------
# CONFIGURAÇÃO
# -----------------------------
# ➡️ Substitua abaixo pelo caminho onde estão suas planilhas .xlsx
pasta = r"Insira o caminho da pasta aqui"

# Nome do arquivo final que será gerado
nome_arquivo_saida = "ID_Compilados_Python.xlsx"

# -----------------------------
# EXECUÇÃO
# -----------------------------

# Procura todos os arquivos .xlsx dentro da pasta
arquivos = glob.glob(os.path.join(pasta, "*.xlsx"))

if not arquivos:
    print("⚠️ Nenhum arquivo .xlsx encontrado na pasta informada.")
else:
    print(f"📂 {len(arquivos)} arquivos encontrados. Iniciando unificação...")

    # Lê todos os arquivos e junta em um único DataFrame
    dfs = [pd.read_excel(arq) for arq in arquivos]
    df_final = pd.concat(dfs, ignore_index=True)

    # Caminho completo do arquivo final
    saida = os.path.join(pasta, nome_arquivo_saida)

    # Salva em Excel
    df_final.to_excel(saida, index=False)
    print(f"✅ Planilhas unificadas com sucesso!")
    print(f"💾 Arquivo salvo em: {saida}")
