import numpy as np

def filtro_base(df, mes_num=None, ano=None,orgao_superior =None, orgao_entidade_vinculada=None):

    if mes_num is not None:
        df =  df.query("mes_num == @mes_num")
    if ano is not None:
        df = df.query("ano == @ano")
    if orgao_superior is not None:
        df = df.query("orgao_superior == @orgao_superior")
    if orgao_entidade_vinculada is not None:
        df = df.query("orgao_entidade_vinculada == @orgao_entidade_vinculada")
    return df

def quantidade_num(quantidade):
    if quantidade is None or quantidade <=0:
        quantidade=1
    return quantidade

#indica em porcentagem o serviço ou produto entregue
def taxa_liquidacao(df, mes_num=None, ano_num=None, quantidade=None):
    qtd = quantidade_num(quantidade)
    base = filtro_base(df, mes_num, ano_num)
    return ( base
            .groupby('orgao_superior', as_index=False)
            .agg(
                 valor_empenhado_total = ('valor_empenhado','sum'),
                 valor_liquidado_total = ('valor_liquidado','sum'))
            .assign(taxa_liquidacao = lambda x: np.where(
                x['valor_empenhado_total'] > 0, ((x['valor_liquidado_total'] / x['valor_empenhado_total'])*100).round(2),
                np.nan
            ))
            .sort_values('taxa_liquidacao', ascending=False)
            .head(qtd)
            .reset_index(drop=True)
            )

def taxa_pagamento(df, mes_num=None, ano_num=None,quantidade=None):
    qtd = quantidade_num(quantidade)
    base = filtro_base(df,mes_num, ano_num, quantidade)
    return (base
            .groupby('orgao_superior', as_index=False)
            .agg(
                 valor_liquidado_total=('valor_liquidado','sum'),
                 valor_pago_total=('valor_pago', 'sum')
            )
            .assign(taxa_pagamento = lambda x:(
                    np.where(
                    x['valor_liquidado_total'] > 0, ( (x['valor_pago_total'] / x['valor_liquidado_total']) *100 ).round(2),
                     np.nan) )
            )
            .sort_values('taxa_pagamento', ascending=False)
            .head(qtd)
            .reset_index(drop=True)
            )

def eficiencia_orcamentaria(df, mes_num=None, ano=None, quantidade=None):
    base = filtro_base(df, mes_num, ano)
    qtd = quantidade_num(quantidade)

    return (
        base
        .groupby('orgao_superior', as_index=False)
        .agg(
            valor_empenhado_total=('valor_empenhado','sum'),
            valor_pago_total = ('valor_pago','sum')
        )
        .assign(
            eficiencia_pagamento = lambda x:(
                np.where(
                x['valor_empenhado_total']>0,
                ( (x['valor_pago_total']/x['valor_empenhado_total']) *100 ).round(2), np.nan )
            )
        )
        .sort_values('eficiencia_pagamento', ascending=False)
        .head(qtd)
        .reset_index(drop=True)
    )

def top_orgaos_pagamento(df, mes_num=None, ano=None):
    return df

def top_entidades_empenho(df, mes_num=None):
    return df

def evolucao_pagamentos(df, mes_num=None):
    return df

def concentracao_pagamento(df, mes_num=None):
    return df

def alerta_restos_altos(df, mes_num=None):
    return df


def criar_metricas(df, mes_num=None) -> dict:
    return {
       'taxa_liquidacao': taxa_liquidacao(df, mes_num),
        'taxa_pagamento': taxa_pagamento(df, mes_num),
        'eficiencia_orcamentaria': eficiencia_orcamentaria(df, mes_num),
        'top_orgaos_pagamento': top_orgaos_pagamento(df, mes_num),
        'top_entidades_empenho': top_entidades_empenho(df, mes_num),
        'evolucao_pagamentos': evolucao_pagamentos(df, mes_num),
        'concentracao_pagamento': concentracao_pagamento(df, mes_num),
        'alerta_restos_altos': alerta_restos_altos(df, mes_num)
    }
