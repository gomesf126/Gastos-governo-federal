import logging
logger = logging.getLogger(__name__)

def validar_colunas(df, arquivo):
    SCHEMA = [
        'Mês Ano',
        'Órgão Superior',
        'Órgão/Entidade Vinculada',
        'Valor Empenhado',
        'Valor Liquidado',
        'Valor Pago',
        'Valor Restos a Pagar Pagos'
    ]
    coluna       = set(df.columns)
    obrigatorias = set(SCHEMA)

    faltantes = obrigatorias - coluna
    extras    = coluna - obrigatorias

    if faltantes:
        raise ValueError(f"Arquivo {arquivo.name} com colunas {faltantes} faltando")
    if extras:
        logger.warning(f"Arquivo {arquivo.name} possui colunas extras: {extras}")