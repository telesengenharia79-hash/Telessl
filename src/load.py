import sqlite3
import pandas as pd


def load(df: pd.DataFrame, db_path: str, tabela: str = "vendas") -> None:
    """Grava o DataFrame em uma tabela SQLite."""
    with sqlite3.connect(db_path) as conn:
        df.to_sql(tabela, conn, if_exists="replace", index=False)


def run_query(db_path: str, sql: str) -> pd.DataFrame:
    """Executa uma consulta SQL e devolve um DataFrame."""
    with sqlite3.connect(db_path) as conn:
        return pd.read_sql(sql, conn)
