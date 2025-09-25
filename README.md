# 🐍 Unificador de Planilhas Excel

Script simples em **Python** para unir várias planilhas `.xlsx` que possuem a mesma estrutura (mesmos nomes de colunas) em um único arquivo Excel.

💡 Ideal para quem precisa consolidar relatórios espalhados em uma pasta em apenas um arquivo final.

---

## 🚀 Como funciona

1. Procura todos os arquivos **.xlsx** dentro da pasta que você definir.
2. Lê cada planilha e armazena em uma lista de DataFrames.
3. Junta todos os DataFrames em um único DataFrame.
4. Salva o resultado em um arquivo chamado **`ID_Compilados_Python.xlsx`** na mesma pasta.

---

## 🛠️ Pré-requisitos

- **Python 3** instalado  
- Bibliotecas **pandas** e **openpyxl**

Instale as dependências executando:

```bash
pip install pandas openpyxl
```

---

## 📂 Como usar

1. **Baixe ou clone este repositório.**  
2. **Abra o arquivo** `unir_planilhas.py` **no seu editor de código.**  
3. **Altere a variável** `pasta` **para o caminho onde estão suas planilhas Excel:**

```python
pasta = r"Insira o caminho da pasta aqui"
```

💡 Exemplos de caminho:

Windows:
```python
pasta = r"C:\Users\SeuUsuario\Desktop\MinhasPlanilhas"
```

Linux/Mac:
```python
pasta = r"/home/usuario/planilhas"
```

4. **Salve o arquivo e execute:**

```bash
python unir_planilhas.py
```

5. Ao finalizar, será criado o arquivo **`ID_Compilados_Python.xlsx`** dentro da mesma pasta.

---

## ✅ Resultado

- Todas as planilhas encontradas serão combinadas em uma única planilha final.
- As colunas precisam ter **nomes iguais** para que a junção seja feita corretamente.

---

## ✨ Autor

Feito com 💻 + ☕ por **Marcelo da Silva Mendonça**  
[GitHub](https://github.com/marcelao-dev) • [LinkedIn](https://www.linkedin.com/in/marcelo-mendon%C3%A7a-46ab37173)
