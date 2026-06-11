def filtro_base(df, mes_num=None, ano=None,orgao_superior =None, orgao_entidade_vinculada=None ):

    if mes_num is not None:
        df =  df.query("mes_num == @mes_num")
    if ano is not None:
        df = df.query("ano == @ano")
    if orgao_superior is not None:
        df = df.query("orgao_superior == @orgao_superior")
    if orgao_entidade_vinculada is not None:
        df = df.query("orgao_entidade_vinculada == @orgao_entidade_vinculada")
    return df

def taxa_liquidacao(df, mes_num=None):
    return df

def taxa_pagamento(df, mes_num=None):
    return df

def eficiencia_orcamentaria(df, mes_num=None):
    return df

def top_orgaos_pagamento(df, mes_num=None):
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
