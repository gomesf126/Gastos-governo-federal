from src.transform.limpeza import (
padronizar_colunas,
tratar_texto,
tratar_numeros,
tratar_nulos_numeros,
tratar_negativos,
resumo_nulos,
flags_nulos,
tratar_nulos,
resumo_duplicados,
remover_duplicatas,
tratar_datas,
remover_colunas_invalidas
)
CLEANING = [
    padronizar_colunas,
    tratar_texto,
    tratar_numeros,
    tratar_nulos_numeros,
    tratar_negativos,
    resumo_nulos,
    flags_nulos,
    tratar_nulos,
    resumo_duplicados,
    remover_duplicatas,
    tratar_datas,
    remover_colunas_invalidas
]

ENGINEERING = [

]

def criar_pipeline(df, etapas):
    for funcao in etapas:
        df = funcao(df)
    return df