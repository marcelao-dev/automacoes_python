# 🐍 Unificador de Planilhas Excel

Script simples em **Python** para unir várias planilhas `.xlsx` que possuem a mesma estrutura (mesmos nomes de colunas) em um único arquivo Excel.

Ideal para quem precisa consolidar relatórios espalhados em uma pasta em apenas um arquivo final.

---

## 🚀 Como funciona

O código:

1. Procura todos os arquivos **.xlsx** dentro de uma pasta que você definir.  
2. Lê cada planilha e armazena em uma lista de DataFrames.  
3. Junta todos os DataFrames em um único.  
4. Salva o resultado em um arquivo chamado `ID_Compilados_Python.xlsx` na mesma pasta.

---

## 🛠️ Pré-requisitos

- Python 3 instalado
- Biblioteca **pandas** e **openpyxl** (para ler e salvar arquivos Excel)

Instale as dependências com:

```bash
pip install pandas openpyxl
