from pathlib import Path
import pandas as pd


def extract(caminho: str) -> pd.DataFrame:
    """Lê um arquivo CSV ou JSON e devolve um DataFrame."""
    ext = Path(caminho).suffix.lower()
    if ext == ".csv":
        return pd.read_csv(caminho)
    if ext == ".json":
        return pd.read_json(caminho)
    raise ValueError(f"Formato não suportado: {ext}")
