from src.config.caminhos import DATA_RAW
from src.config.logging_config import logging
import pandas as pd
from src.extract.colunas import validar_colunas

logger = logging.getLogger(__name__)

def extrair():
    try:
        arquivos =  sorted(DATA_RAW.glob("*.csv"), key=lambda x: x.stat().st_mtime, reverse=True)

        if not arquivos:
            raise FileNotFoundError('Nenhum arquivo csv encontrado')

        arquivo = arquivos[0]

        df = pd.read_csv(arquivo, sep=';' , encoding='utf-8')
        logger.info(f"Arquivo carregado com sucesso {arquivo.name}")

        validar_colunas(df, arquivo)
        logger.info("Colunas validadas com sucesso")

    except Exception as error:
        logger.error(f"Erro ao processar o arquivo {arquivo.name}: {error}")
        raise

    return df

