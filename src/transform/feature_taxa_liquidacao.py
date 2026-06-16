import numpy as np
# Calcula a taxa de liquidação,
# indicando quanto do orçamento empenhado
# foi entregue em bens ou serviços.
def feature_taxa_liquidacao(df):
    df =  df.assign(
          taxa_liquidacao = lambda x: np.where (
          x['valor_empenhado'] > 0,
          x['valor_liquidado'] / x['valor_empenhado'],
          np.nan ))

    return df

