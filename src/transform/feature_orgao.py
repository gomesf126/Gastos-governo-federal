
def feature_orgao(df):
    return df
#ranking_orgao
#gasto_total_orgao
#media_pagamento_orgao

#produto → faturamento / órgão → valor pago
#faturamento_total -> total_pago
#top_produtos -> top_orgaos
#top_clientes -> top_entidades
#classe_abc_produto -> classe_abc_orgao
#churn_cliente -> inatividade_orgao

"""Top Órgãos por:
- Empenho
- Liquidação
- Pagamento
- Restos a pagar"""

"""O que significa

Órgão sem movimentação recente:

não empenhou
não liquidou
não pagou

durante um período."""

""" Valor Restos a Pagar Pagos

São pagamentos de dívidas de anos anteriores.

Exemplo:

Serviço feito em 2025
mas pago em 2026"""