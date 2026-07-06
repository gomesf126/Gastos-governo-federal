import matplotlib.pyplot as plt
from src.extract.extrair import extrair
from src.pipeline.pipeline import pipeline
from src.analytics.metricas import  taxa_liquidacao
from src.analytics.color import AZUL,CINZA,VERDE,LARANJA,VERMELHO, FUNDO,GRID

df = extrair()
df = pipeline(df)

liquidacao = taxa_liquidacao(df , quantidade=6)



#==============================================================
def graficos(liquidacao):
    liquidacao = liquidacao.copy()
    liquidacao['orgao_curto'] = ( liquidacao['orgao_superior'].str.slice(0, 25).add('...'))

    maior_valor = liquidacao['valor_liquidado_total'].max()

    #DESTACAR
    cores = [
        AZUL if valor != maior_valor else LARANJA
        for valor in liquidacao['valor_liquidado_total']
    ]
    #CONFIGURAÇÃO
    plt.style.use('ggplot')
    fig  = plt.figure(figsize=(15,8) ,  constrained_layout=True)
    gs = fig.add_gridspec(nrows=1, ncols=2 )

    ax0 = fig.add_subplot(gs[0,:])

    #GRAFICO
    fig.suptitle(
        "Dashboard Orçamentário do Governo Federal",
        fontsize=18,
        fontweight="bold",
        color=CINZA

    )    #Criar espaço acima do gráfico
    #fig.subplots_adjust( top=1.8, left=0.07, right=0.98, bottom=0.15 )

    #GRAFICO
    ax0.bar(liquidacao['orgao_curto'],
            liquidacao['valor_liquidado_total'],
             color=cores,
             alpha=0.8,
             width=0.65
            )

    ax0.grid( axis='x', visible=False )

    ax0.set_title('Produtos e serviços confirmados ' ,color=CINZA, fontsize=12, pad=16, fontweight="semibold", loc='left')

    #vitar que os nomes encostem um no outro
    plt.setp(
        ax0.get_xticklabels(), rotation=10,ha='right'
    )

    ax0.spines['left'].set_visible(False)
    ax0.spines['top'].set_visible(False)
    ax0.spines['right'].set_visible(False)
    ax0.set_yticks([])

    ax0.margins(y=0.25)


    ofset= maior_valor * 0.02

    for x , y in zip(liquidacao['orgao_curto'], liquidacao['valor_liquidado_total']):
        valor =(
            f'R$ {y:,.2f}'
            .replace(',','x')
            .replace('.',',')
            .replace('x','.')
        )
        ax0.text(
            x,
            y + ofset,
            valor,
            ha='center',
            fontweight='bold',
            fontsize=10,
            color=CINZA
        )
    plt.show()






graficos(liquidacao)