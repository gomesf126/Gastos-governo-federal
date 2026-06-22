import numpy as np
# Calcula a eficiência orçamentária,
# indicando quanto do orçamento empenhado
# foi efetivamente pago.
def feature_taxa_pagamento(df):
    df = df.assign(
        taxa_pagamento = lambda x: np.where(
            x['valor_liquidado_total'] > 0,
            x['valor_pago_total'] / x['valor_liquidado_total'],
            np.nan)
    )
    return df