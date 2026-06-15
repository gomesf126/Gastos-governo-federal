import numpy as np
# Cria uma feature que mede, em porcentagem,
# quanto do valor empenhado foi efetivamente entregue
# e reconhecido pela administração pública.
def feature_alerta_restos_altos(df):
    df = df.assign(
        alerta_empenhos_altos = lambda x:
        np.where(
            x['valor_empenhado'] > 0,
            (x['valor_empenhado'] - x['valor_liquidado']) / x['valor_empenhado'],
            np.nan
        ),
        alerta_restos_altos = lambda x: np.where(
            x['alerta_empenhos_altos'] > 0.50, 1 , 0
        )

    )
    return df