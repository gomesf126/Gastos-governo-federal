import pandas as pd
from src.extract.extrair import extrair
from src.pipeline import pipeline
from src.analytics.metricas import criar_metricas

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)