# Calcula o valor empenhado que ainda não foi liquidado,
# indicando a parcela dos bens ou serviços que ainda
# não foram entregues ou reconhecidos pela administração.
def feature_saldo_liquidar(df):
    df = df.assign(
        saldo_liquidar =  lambda x: x['valor_empenhado_total'] - x['valor_liquidado_total']
    )
    return df
