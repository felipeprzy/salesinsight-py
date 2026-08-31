

## mini projeto  - M1S08  

# SalesInsight PY

## Sobre o projeto
Análise e visualização de dados de vendas desenvolvida em Python. 
O projeto carrega, limpa, transforma, agrega e visualiza um dataset de vendas, gerando métricas por período, produto, categoria e região, além de uma segmentação de clientes por faixa de gasto.

## O que o projeto analisa
- Receita total e volume de vendas por mês e por trimestre
- Top produtos e categorias por receita
- Desempenho por região
- Segmentação de clientes por nível de gasto (Bronze, Prata, Ouro)
- Operações numéricas vetorizadas com NumPy (media, mediana, desvio padrão, broadcasting, filtragem booleana)
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

Optei por remover registros com dados inválidos (datas inválidas, nulos em quantidade e preco_unitario) em vez de preenchê-los com algum valor estimado. 
Para verificar a questão da limpeza, em cada etapa os problemas são contados e armazenados antes de serem removidos, no final monto um relatório mostrando quantas linhas eu tinha no início, quantas caíram por data inválida, quantas por nulo em quantidade, quantas por nulo em preço, e quantas tinham os dois problemas ao mesmo tempo. A soma de tudo que foi removido tem que bater exatamente com a diferença entre o total inicial e o final.
Quando verifiquei o resultado do regex para limpeza dos nomes (utilizando "re.sub"), vi que a limpeza não resolveu. Os caracteres "ruins" foram apagados, mas não foi substituído pelo caractere do padrão do nome (Cliente_NNN) , então resolvi considerar apenas o número do campo nome e criar o padrão da nomenclatura (utilizando o "re.findall")
Ao segmentar clientes foram usados limites via lambda ( "Bronze" if < 5000 else ("Prata" if  < 15000 else "Ouro") ).
Na parte de criar o analizador de vendas, a lógica utilizada foi "grudando" o método na classe ( def limpar(self) ), ao invés dos métodos escritos direto dentro do corpo da classe ( class AnalisadorDeVendas: ... def__init__(self, caminho_arquivo): ... def carregar(self): ... def limpar(self): ).
Foi feito um bloco adicional com a criação de uma tabela mestra ( adicionando o segmento de cliente como coluna via groupby().transform("sum") ) no lugar do usado na classe principal ( merge ). A idéia foi de analizar os dados de forma semelhante a uma planilha dinâmica, o que trouxe mais informações analíticas sobre os dados.


## Ferramentas utilizadas
- Python 3.14
- VS Code
- Bibliotecas: pandas, numpy, matplotlib, seaborn (nativas: re, json, os)
- GitHub e GitHub Desktop para versionamento

## Respostas as perguntas
Há uma queda brusca nos meses 6,7 e começou a recuperar após o mês 8, o que afeta o trimestre mas fica "diluído" no cálcuolo do trimestre, bem como as vendas do mês 5 e 11. No primeiro trimestre tendência de queda, no segundo alta volatilidade, no terceiro recuperação nas vendas, fechando com a maior venda mensal e o início da retração.
Os produtos / catergorias que geram maiores receitas são computadores.
As regiões de maior desempenho são: Norte em primeiro lugar, sudeste e sul.
Os clientes mais valiosos são os Ouro, com uma representatividade muito maior em todos os aspectos.
A relação maior é com a categoria (computadores) e com o segmento de cliente (ouro) do que a quantidade vendida. Com relação as transações, existe uma correlação positiva.

## Vídeo de demonstração
https://drive.google.com/file/d/1WmsIASCVd3NDXldCChjEB_IqeErZ8C0T/view?usp=sharing

## Repositório público no GitHub: 
https://github.com/felipeprzy/salesinsight-py