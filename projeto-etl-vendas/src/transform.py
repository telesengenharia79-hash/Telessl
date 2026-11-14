import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Limpa e enriquece os dados."""
    df = df.drop_duplicates()
    df = df.dropna(subset=["quantidade"])
    df["quantidade"] = df["quantidade"].astype(int)
    df["data_venda"] = pd.to_datetime(df["data_venda"])
    df["valor_total"] = df["quantidade"] * df["preco_unitario"]
    return df
