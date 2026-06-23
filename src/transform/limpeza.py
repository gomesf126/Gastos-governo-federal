import pandas as pd
import unicodedata
import numpy as np

def padronizar_colunas(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("/","_")
    )
    df.columns = [
        unicodedata.normalize("NFKD", col)
        .encode("ASCII", 'ignore')
        .decode('utf-8')
        for col in df.columns
        ]
    df = df.rename(columns={'valor_restos_a_pagar_pagos': 'atrasados_pagos'})
    return df



def tratar_texto(df):
    #pandas procura colunas que possuem tipos de texto
    colunas_texto = df.select_dtypes(include=['object','string']).columns

    #percorre cada coluna de texto e aplica transformações.
    df[colunas_texto] = df[colunas_texto].apply(
        lambda col: col.astype('string')
        .str.strip()
        .str.title()
    )

    return df

def tratar_numeros(df):
    colunas_valores = ['valor_empenhado','valor_liquidado', 'valor_pago','atrasados_pagos']

    colunas_existentes =[]
    for col in colunas_valores:
        if col in df.columns:
            colunas_existentes.append(col)

    df[colunas_existentes]= df[colunas_existentes].apply(
        lambda col: col.astype('string')
        .str.replace(r'[^\d,.-]','', regex=True)
        .str.replace('.','', regex=False)
        .str.replace(',','.', regex=False)
        .str.strip()
    )

    df[colunas_existentes] = df[colunas_existentes].apply(
        pd.to_numeric , errors='coerce'
    )
    return df

def tratar_negativos(df):
    colunas_valores = ['valor_empenhado','valor_liquidado', 'valor_pago','atrasados_pagos']

    colunas_existentes=[
        col for col in colunas_valores
        if col in df.columns
    ]

    for col in colunas_existentes:
        df[f'{col}_negativo'] = np.where(df[col] < 0, 1, 0)
    return df


def tratar_nulos_numeros(df):
    colunas_valores = ['valor_empenhado', 'valor_liquidado', 'valor_pago', 'atrasados_pagos']

    colunas_existentes = [
        col for col in colunas_valores
        if col in df.columns
    ]

    for col in colunas_existentes:
        df[col] = df[col].fillna(0).astype('Float64')
    return df


def tratar_nulos(df):

    return df.assign(
        orgao_superior = lambda col: col['orgao_superior'].fillna('sem_orgao_superior'),
        orgao_entidade_vinculada = lambda col: col['orgao_entidade_vinculada'].fillna('sem_orgao_entidade')
    )
def flags_nulos(df):
    colunas = ['mes_ano', 'orgao_superior', 'orgao_entidade_vinculada',
       'valor_empenhado', 'valor_liquidado', 'valor_pago', 'atrasados_pagos']

    for col in colunas:
        if col in df.columns:
            df[f"{col}_nulo"] = df[col].isna()

    return df

def resumo_nulos(df):
    colunas = ['mes_ano', 'orgao_superior', 'orgao_entidade_vinculada',
       'valor_empenhado', 'valor_liquidado', 'valor_pago', 'atrasados_pagos']
    dados = []
    for col in colunas:
        if col in df.columns:
            dados.append(
                {
                    'coluna': col,
                    'quantidade_nulos': df[col].isna().sum(),
                    'percentual_nulos': round(df[col].isna().mean() * 100, 2)
                }
            )
    return pd.DataFrame(dados)

def tratar_datas(df):
    df = df.assign(mes_ano = lambda x: pd.to_datetime(x['mes_ano'] ,format='%m/%Y', errors='coerce') )
    return df

def resumo_duplicados(df):
    dados = {
        'total_linhas': len(df),
        'linhas_duplicadas': df.duplicated().sum(),
        'percentual_duplicados': round(df.duplicated().mean() * 100, 2)
    }
    return pd.DataFrame([dados])

def tipos_dados(df):
    return pd.DataFrame(
        {
            'coluna':df.dtypes.index,
            'tipo':df.dtypes.astype(str).values
        }
    )


def remover_duplicatas(df):
    return df.drop_duplicates()#.reset_index(drop=True)

def remover_colunas_invalidas(df):
    return df.iloc[:,~df.columns.str.contains('^unnamed', case=False)]
