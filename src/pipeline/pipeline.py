from src.transform.features import criar_pipeline,criar_resumos
from src.transform.features import CLEANING, ENGINEERING

def pipeline(df):
 return(
     df
     #CLEANING
     .pipe(criar_pipeline, CLEANING)
     #ENGINEERING
     .pipe(criar_pipeline, ENGINEERING)
 )

def pipeline_resumos(df):
    return criar_resumos(df)