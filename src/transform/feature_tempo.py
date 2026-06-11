
mapa_mes ={
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho',
    7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}
mapa_trimestre =  {
    1:'1° Trimestre',
    2:'2° Trimestre',
    3:'3° Trimestre',
    4:'4° Trimestre'
}
def feature_tempo(df):
    return df.assign(
        data_pagamento   = lambda x: x['mes_ano'],
        mes              = lambda x: x['mes_ano'].dt.month.map(mapa_mes),
        mes_num          = lambda x: x['mes_ano'].dt.month,
        ano              = lambda x: x['mes_ano'].dt.year,
        trimestre_num    =lambda x: x['mes_ano'].dt.quarter,
        trimestre        = lambda x: x['mes_ano'].dt.quarter.map(mapa_trimestre)

    )