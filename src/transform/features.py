from src.transform.limpeza import resumo_nulos,resumo_duplicados

from src.transform.limpeza import (
    padronizar_colunas,
    tratar_texto,
    tratar_numeros,
    tratar_nulos_numeros,
    tratar_negativos,
    flags_nulos,
    tratar_nulos,
    remover_duplicatas,
    tratar_datas,
    remover_colunas_invalidas
)
from src.transform.feature_taxa_liquidacao import feature_taxa_liquidacao
from src.transform.feature_taxa_pagamento import feature_taxa_pagamento
from src.transform.feature_saldo_liquidar import feature_saldo_liquidar
from src.transform.feature_tempo import feature_tempo
from src.transform.feature_eficiencia_orcamentaria import feature_eficiencia_orcamentaria
from src.transform.feature_classe_abc_valor_liquidado import feature_classe_abc_valor_liquidado
from src.transform.feature_alertas_empenhos_altos import feature_alertas_empenhos_altos
from src.transform.churn_inatividade_orgao import churn_inatividade_orgao

CLEANING = [
    padronizar_colunas,
    tratar_texto,
    tratar_numeros,
    tratar_nulos_numeros,
    tratar_negativos,
    flags_nulos,
    tratar_nulos,
    remover_duplicatas,
    tratar_datas,
    remover_colunas_invalidas
]

ENGINEERING = [
    feature_tempo,
    churn_inatividade_orgao,
    feature_classe_abc_valor_liquidado,
    feature_taxa_liquidacao,
    feature_taxa_pagamento,
    feature_saldo_liquidar,
    feature_eficiencia_orcamentaria,
    feature_alertas_empenhos_altos
    ]


def criar_resumos(df):
    return {
        'nulos': resumo_nulos(df),
        'duplicados': resumo_duplicados(df)
    }

def criar_pipeline(df, etapas):
    for funcao in etapas:
        df = funcao(df)
    return df
