from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / 'data'

DATA_RAW = DATA_DIR / 'raw'
DATA_PROCESSED = DATA_DIR / 'processed'

DATA_RAW.mkdir(parents=True, exist_ok=True)
DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
