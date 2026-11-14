from pathlib import Path
from src.extract import extract
from src.transform import transform
from src.load import load, run_query

ARQUIVO = "data/raw/vendas.csv" 
DB = "vendas.db"

df = extract(ARQUIVO)
print(f"Extraído: {len(df)} linhas")

df = transform(df)
print(f"Transformado: {len(df)} linhas")

load(df, DB)
print(f"Carregado em {DB}\n")


for consulta in Path("sql/queries.sql").read_text().split(";"):
    if consulta.strip():
        print(run_query(DB, consulta), "\n")
