

## mini projeto  - M1S08  

# SalesInsight PY

## Sobre o projeto
Analise e visualização de dados de vendas desenvolvida em Python. O
projeto carrega, limpa, transforma, agrega e visualiza um dataset de
vendas, gerando métricas por período, produto, categoria e região,
além de uma segmentação simples de clientes por faixa de gasto.

## O que o projeto analisa
- Receita total e volume de vendas por mês e por trimestre
- Top produtos e categorias por receita
- Desempenho por região
- Segmentação de clientes por nível de gasto (Bronze, Prata, Ouro)
- Operações numéricas vetorizadas com NumPy (media, mediana, desvio
  padrão, broadcasting, filtragem booleana)
- Exportação de relatórios em CSV e JSON, e de gráficos em PNG

## Conceitos aplicados (Modulo 01 - Semanas 01 a 08)
- Logica de programação: variáveis, tipos, operadores, condicionais
- Estruturas de dados: listas, tuplas, dicionários e estruturas compostas
- Funções: parâmetros, retorno, docstrings, lambda, ordem superior
- Leitura e escrita de arquivos CSV e JSON
- Modulo datetime e expressões regulares (re)
- Pandas: Series, DataFrames, filtros, groupby, transformações
- NumPy: arrays, operações vetorizadas e broadcasting
- Matplotlib e Seaborn: linha, barra, dispersao, subplots, export
- Introdução a classes: construtor, atributos e métodos
- Git e GitHub: branches, commits e GitFlow simplificado

## Como executar

### Localmente com VS Code
1. Instale o Python 3.10 ou superior.
2. Instale as dependências:

pip install -r requirements.txt

3. Execute no terminal:

python salesinsight.py


O script gera automaticamente o `vendas.csv` (dataset sintetico) caso
o arquivo ainda não exista, e cria a pasta `outputs/` com todos os
relatórios e gráficos.

## Estrutura do projeto

salesinsight-py/
|-- salesinsight.py # fluxo principal (funções + classe + main)
|-- vendas.csv # dataset (gerado automaticamente)
|-- requirements.txt
|-- README.md
|-- outputs/
| |-- metricas_por_mes.csv
| |-- segmentacao_clientes.csv
| |-- estatisticas_gerais.json
| |-- gráficos/
| |-- receita_por_mes.png
| |-- top_produtos.png
| |-- quantidade_vs_receita.png
| |-- painel_resumo.png


## Decisões técnicas
Optei por remover registros com dados inválidos (datas invalidas,
nulos em quantidade e preco_unitario) em vez de preenchê-los com
algum valor estimado. O relatório de limpeza
detalha exatamente quantos registros foram removidos e por qual
motivo, permitindo auditar o processo.

## Ferramentas utilizadas
- Python 3.14
- VS Code
- Bibliotecas: pandas, numpy, matplotlib, seaborn (nativas: re, json, os)
- GitHub e GitHub Desktop para versionamento

## Vídeo de demonstração
[inserir o link aqui apos gravar]