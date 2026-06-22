import numpy as np
# Identifica os órgãos que concentram a maior parte
# do valor liquidado por meio da Curva ABC.
#
# Classe A: até 80% do valor liquidado acumulado.
# Classe B: de 80% até 95%.
# Classe C: acima de 95%.
def feature_classe_abc_valor_liquidado(df):
    abc = ( df
            [['orgao_superior','valor_liquidado_total']]
            .drop_duplicates('orgao_superior')
            .sort_values('valor_liquidado_total', ascending=False)
            .reset_index(drop=True)
            .assign(
                percentual_orgao = lambda x:
                x['valor_liquidado_total'] /
                x['valor_liquidado_total'].sum(),
                percentual_acumulado = lambda x: x['percentual_orgao'].cumsum()
            )
    )

    abc['classe_abc'] = np.select(
        [
            abc['percentual_acumulado'] <= 0.80,
            abc['percentual_acumulado'] <= 0.95
        ],
        ['A','B'],
        default='C'
    )
    return df.merge(
        abc[['orgao_superior','classe_abc','percentual_orgao','percentual_acumulado']],
        on='orgao_superior',
        how='left'
    )
