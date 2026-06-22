import numpy as np
def feature_eficiencia_orcamentaria(df):
    df =df.assign(
    # eficiencia_orcamentaria:
    # mede a proporção do valor empenhado que foi efetivamente pago.
        eficiencia_orcamentaria = lambda x: np.where(
            x['valor_empenhado_total'] > 0,
            x['valor_pago_total'] / x['valor_empenhado_total'],
            np.nan
        ),
    #excesso_pagamento: calcula o valor pago acima do valor empenhado.
        excesso_pagamento = lambda x:  np.where(
            x['valor_pago_total'] > x['valor_empenhado_total'],
            x['valor_pago_total'] - x['valor_empenhado_total'],
            0
        ),
    #flag_excesso_pagamento: identifica registros em que o valor pago  supera o valor empenhado.
        flag_excesso_pagamento = lambda x: np.where(
            x['valor_pago_total'] > x['valor_empenhado_total'],
            1,
            0
        )
    )
    return df
#Quantos registros tiveram excesso?
#Quais órgãos tiveram excesso?
#Qual o valor total excedente?