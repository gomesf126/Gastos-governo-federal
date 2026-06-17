import pandas as pd
from src.extract.extrair import extrair
from src.pipeline.pipeline import pipeline , criar_resumos
from src.analytics.metricas import criar_metricas


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def main():
    df = extrair()
    resumos = criar_resumos(df)
    df = pipeline(df)

    metrica = criar_metricas(df)
    print(resumos)

    return df
if __name__ == '__main__':
    main()