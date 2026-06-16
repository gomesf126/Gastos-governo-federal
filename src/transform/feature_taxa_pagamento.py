import numpy as np
# Calcula a eficiência orçamentária,
# indicando quanto do orçamento empenhado
# foi efetivamente pago.
def feature_taxa_pagamento(df):
    df = df.assign(
        taxa_pagamento = lambda x: np.where(
            x['valor_liquidado'] > 0,
            x['valor_pago'] / x['valor_liquidado'],
            np.nan)
    )
    return df