import numpy as np
import pandas as pd

pd.options.display.float_format ='{:,.2f}'.format

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
            [['orgao_superior',
              'valor_empenhado_total',
              'valor_liquidado_total',
              'taxa_liquidacao']]
            .drop_duplicates('orgao_superior')
            .sort_values('taxa_liquidacao')
            .head(qtd)
            .reset_index(drop=True)
            )

def taxa_pagamento(df, mes_num=None, ano_num=None,quantidade=None):
    qtd = quantidade_num(quantidade)
    base = filtro_base(df,mes_num, ano_num, quantidade)
    return (base
            [['orgao_superior',
              'valor_liquidado_total',
              'valor_pago_total',
              'taxa_pagamento']]
            .drop_duplicates('orgao_superior')
            .sort_values('taxa_pagamento', ascending=False)
            .head(qtd)
            .reset_index(drop=True)
            )

def eficiencia_orcamentaria(df, mes_num=None, ano=None, quantidade=None):
    base = filtro_base(df, mes_num, ano)
    qtd = quantidade_num(quantidade)

    return (
        base
        [['orgao_superior',
          'valor_empenhado_total',
          'valor_pago_total',
          'eficiencia_orcamentaria',
          'excesso_pagamento',
          'flag_excesso_pagamento']]
        .drop_duplicates('orgao_superior')
        .sort_values('eficiencia_orcamentaria', ascending=False)
        .head(qtd)
        .reset_index(drop=True)
    )

def feature_saldo_liquidar(df, mes_num=None, ano=None, quantidade= None):
    quantidade = quantidade_num(quantidade)
    base = filtro_base(df, mes_num, ano)
    return(
        base
        [['orgao_superior',
          'valor_empenhado_total',
          'valor_liquidado_total',
          'saldo_liquidar']]
        .drop_duplicates('orgao_superior')
        .sort_values('saldo_liquidar', ascending=False)
        .head(quantidade)
        .reset_index(drop=True)
    )

def evolucao_pagamentos(df, mes_num=None, ano=None, quantidade=None):
    qtd = quantidade_num(quantidade)
    base = filtro_base(df,  ano)
    return (
        base
        .pivot_table(
            index=['orgao_superior','ano'],
            columns=['mes_num','mes'],
            values='valor_pago',
            aggfunc='sum'
        )
        .reset_index()
        .sort_values(['orgao_superior'])
        .head(qtd)
    )



def concentracao_pagamento(df, mes_num=None, ano=None, quantidade=None):
    qtd= quantidade_num(quantidade)
    base = filtro_base(df,mes_num,ano)
    return (
        base
        [['orgao_superior',
          'valor_empenhado_total',
          'valor_pago_total',
          'valor_atrasados_pagos_total']]
        .drop_duplicates('orgao_superior')
        .sort_values('valor_pago_total', ascending=False)
        .head(qtd)
        .reset_index(drop=True)
    )

def alertas_empenhos_altos(df, mes_num=None, ano=None, quantidade=None):
    qtd= quantidade_num(quantidade)
    base = filtro_base(df,mes_num,ano)
    return(
        base
        [['orgao_superior',
          'valor_empenhado_total',
          'valor_liquidado_total',
          'alerta_empenho_alto',
          'flag_alerta_empenho_alto']]
        .drop_duplicates('orgao_superior')
        .sort_values('alerta_empenho_alto', ascending=False)
        .head(qtd)
        .reset_index(drop=True)
    )

def chur_pagamento(df, mes_num=None, ano=None, quantidade=None):
    qtd= quantidade_num(quantidade)
    base = filtro_base(df,mes_num,ano)
    return (
        base
        [['orgao_superior',
          'ultimo_pagamento_orgao',
          'dias_sem_pagamento',
          'status_pagamento']]
        .drop_duplicates('orgao_superior')
        .sort_values('dias_sem_pagamento')
        .head(qtd)
        .reset_index(drop=True)
    )

def classe_abc_valor_liquidado(df, mes_num=None, ano=None, quantidade=None):
    qtd= quantidade_num(quantidade)
    base = filtro_base(df,mes_num,ano)
    return(
        base
        [['orgao_superior',
          'percentual_orgao',
          'percentual_acumulado',
          'classe_abc']]
        .drop_duplicates('orgao_superior')
        .sort_values('classe_abc')
        .head(qtd)
        .reset_index(drop=True)
    )

def criar_metricas(df, mes_num=None, ano=None, quantidade=None) -> dict:
    return {
       'taxa_liquidacao': taxa_liquidacao(df,mes_num,ano,quantidade),
        'taxa_pagamento': taxa_pagamento(df,mes_num,ano,quantidade),
        'eficiencia_orcamentaria': eficiencia_orcamentaria(df,mes_num,ano,quantidade),
        'feature_saldo_liquidar':feature_saldo_liquidar(df,mes_num,ano,quantidade),
        'evolucao_pagamentos': evolucao_pagamentos(df,mes_num,ano,quantidade),
        'concentracao_pagamento': concentracao_pagamento(df,mes_num,ano,quantidade),
        'alertas_empenhos_altos': alertas_empenhos_altos(df,mes_num,ano,quantidade),
        'chur_pagamento':chur_pagamento(df,mes_num,ano,quantidade),
        'classe_abc_valor_liquidado':classe_abc_valor_liquidado(df,mes_num,ano,quantidade)
    }
