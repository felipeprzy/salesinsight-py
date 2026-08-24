import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def gerar_dataset_vendas(n_registros=200, seed=56):
    """Gera um dataset sintético de vendas com dados sujos."""
    random.seed(seed)
    np.random.seed(seed)
    
    produtos = ["Notebook", "Smartphone", "Tablet", "Monitor",
                "Teclado", "Mouse", "Headset"]
    categorias = {"Notebook": "Computadores", "Smartphone": "Celulares",
                  "Tablet": "Celulares", "Monitor": "Computadores",
                  "Teclado": "Perifericos", "Mouse": "Perifericos",
                  "Headset": "Perifericos"}
    precos = {"Notebook": 2500, "Smartphone": 1200, "Tablet": 990,
              "Monitor": 800, "Teclado": 100, "Mouse": 50,
              "Headset": 150}
    regioes = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
    
    data_inicio = datetime(2025, 1, 1)
    dados = []

    for i in range(n_registros):
        produto = random.choice(produtos)
        categoria = categorias[produto]
        quantidade = random.randint(1, 10)
        preco = round(precos[produto] * random.uniform(0.85, 1.15), 2)
        data = data_inicio + timedelta(days=random.randint(0, 364))
        data_txt = data.strftime("%Y-%m-%d")
        cliente = f"Cliente_{random.randint(1, 50):03d}"
                # --- sujeira proposital para a etapa de limpeza ---
        if random.random() < 0.05:
            quantidade = None                    # valor nulo
        if random.random() < 0.04:
            preco = None                          # valor nulo
        if random.random() < 0.06:
            produto = "  " + produto + "  "       # espaços extras
        if random.random() < 0.03:
            data_txt = "DATA INVALIDA"            # data inválida
        if random.random() < 0.10:
            cliente = random.choice([             # ruído no nome
                cliente.upper().replace("_", "-"),
                cliente + "!!",
                " " + cliente,
                cliente.replace("Cliente_", "cliente#"),
            ])
        dados.append({
            "id_venda": i + 1,
            "data_venda": data_txt,
            "cliente": cliente,
            "produto": produto,
            "categoria": categoria,
            "regiao": random.choice(regioes),
            "quantidade": quantidade,
            "preco_unitario": preco,
        })

    return pd.DataFrame(dados)

# Gerar e salvar o CSV bruto
df_bruto = gerar_dataset_vendas()
df_bruto.to_csv("vendas.csv", index=False)
print(f"Dataset gerado com {len(df_bruto)} registros.")
print(df_bruto.head())
            
# agora vou conferir a tabela

def inspecionar_dados(df):
    """Exibe as informacoes estruturais do DataFrame."""
    print("\n=== INSPECAO INICIAL DO DATASET ===")
    print(f"Shape: {df.shape}")
    print(f"\nColunas: {list(df.columns)}")
    print(f"\nTipos de dados:\n{df.dtypes}")
    print(f"\nValores nulos por coluna:\n{df.isnull().sum()}")
    print(f"\nPrimeiros registros:\n{df.head()}")
    return df
        
inspecionar_dados(df_bruto)

# Etapa 1 - limpeza de dados

import re

def limpar_dados(df):
    """
    Limpa e trata o DataFrame de vendas.
    Retorna: (df_limpo, relatorio), onde relatorio e um dicionario
    com as contagens de registros iniciais, removidos e finais.
    """
    df = df.copy()
    n_inicial = len(df)
    
# remover espaços extras em texto

    colunas_texto = ["cliente", "produto", "categoria", "regiao"]
    for col in colunas_texto:
        df[col] = df[col].str.strip()    
    
# teste da Etapa 1
teste = df_bruto.copy()
teste["produto"] = teste["produto"].str.strip()
print(teste["produto"].head(10))

# Etapa 2 — tratar datas inválidas - converter data_venda e descartar as invalidas

teste["data_venda"] = pd.to_datetime(teste["data_venda"], errors="coerce")
n_data_invalida = teste["data_venda"].isna().sum()
teste = teste.dropna(subset=["data_venda"])

# teste da Etapa 2
print("Linhas antes:", len(df_bruto))
print("Datas invalidas encontradas:", n_data_invalida)
print("Linhas depois de remover datas invalidas:", len(teste))

# Etapa 3: remover nulos em quantidade e preco_unitario 
linhas_antes_etapa3 = len(teste)
teste = teste.dropna(subset=["quantidade", "preco_unitario"])

# teste da Etapa 3 
print("Linhas antes da Etapa 3:", linhas_antes_etapa3)
print("Linhas depois de remover nulos:", len(teste))
print("Total removido nesta etapa:", linhas_antes_etapa3 - len(teste))

# Etapa 4: garantir os tipos numericos corretos (inteiro)

teste["quantidade"] = teste["quantidade"].astype(int)
teste["preco_unitario"] = teste["preco_unitario"].astype(float)

# teste da Etapa 4 
print("Tipo de quantidade:", teste["quantidade"].dtype)
print("Tipo de preco_unitario:", teste["preco_unitario"].dtype)
print(teste[["quantidade", "preco_unitario"]].head())

# Etapa 5: padronizar nome do cliente com regex

def padronizar_cliente(nome):
        """Remove tudo que nao for letra, numero ou underline, e ajusta o padrao Cliente_NNN."""
        limpo = re.sub(r"[^A-Za-z0-9_]", "", str(nome))
        limpo = re.sub(r"(?i)cliente", "Cliente", limpo)
        return limpo

teste["cliente"] = teste["cliente"].apply(padronizar_cliente)

# teste da Etapa 5
print(teste["cliente"].head(15))

# correção da Etapa 5 - a v1 deixou "Cliente034" sem underline, ajustando
def padronizar_cliente_v2(nome):
    """Extrai o numero do nome do cliente e reconstroi no padrao Cliente_NNN."""
    digitos = re.findall(r"\d+", str(nome))
    if digitos:
        numero = digitos[0].zfill(3)
        return f"Cliente_{numero}"
    return "Cliente_000"

teste["cliente"] = teste["cliente"].apply(padronizar_cliente_v2)

# Teste da Etapa 5 corrigida
print(teste["cliente"].head(15))

# Etapa 6: relatorio detalhado de limpeza
base_relatorio = df_bruto.copy()
base_relatorio["data_venda"] = pd.to_datetime(base_relatorio["data_venda"], errors="coerce")

linhas_data_invalida = base_relatorio["data_venda"].isna().sum()
base_relatorio = base_relatorio.dropna(subset=["data_venda"])

linhas_nulo_quantidade = base_relatorio["quantidade"].isna().sum()
linhas_nulo_preco = base_relatorio["preco_unitario"].isna().sum()
linhas_nulo_ambos = base_relatorio[
    base_relatorio["quantidade"].isna() & base_relatorio["preco_unitario"].isna()
].shape[0]

base_relatorio = base_relatorio.dropna(subset=["quantidade", "preco_unitario"])

relatorio = {
    "linhas_iniciais": len(df_bruto),
    "removidas_data_invalida": int(linhas_data_invalida),
    "removidas_nulo_quantidade": int(linhas_nulo_quantidade),
    "removidas_nulo_preco_unitario": int(linhas_nulo_preco),
    "removidas_nulo_ambos_ao_mesmo_tempo": int(linhas_nulo_ambos),
    "linhas_finais": len(base_relatorio),
}

# teste da Etapa 6
print("Relatorio de limpeza:")
for chave, valor in relatorio.items():
    print(f"  {chave}: {valor}")