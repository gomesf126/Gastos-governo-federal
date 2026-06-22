def feature_financeira_base(df):
    return (
        df
        .assign(
            valor_empenhado_total = lambda x: x.groupby('orgao_superior')['valor_empenhado'].transform('sum'),
            valor_liquidado_total = lambda x: x.groupby('orgao_superior')['valor_liquidado'].transform('sum'),
            valor_pago_total      = lambda x: x.groupby('orgao_superior')['valor_pago'].transform('sum'),
            valor_atrasados_pagos_total = lambda x: x.groupby('orgao_superior')['atrasados_pagos'].transform('sum')
        )
    )