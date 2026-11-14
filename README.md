# Projeto ETL de Vendas

Pipeline simples: **Extract** (CSV/JSON) → **Transform** (pandas) → **Load** (SQLite) → **Query** (SQL).

## Como rodar
    pip install -r requirements.txt
    python main.py

## Estrutura
- data/raw/      arquivos de entrada
- src/           extract.py, transform.py, load.py
- sql/           consultas SQL
- main.py        orquestra o pipeline

## Próximos passos
- Trocar o CSV por JSON ou uma API
- Adicionar logs e testes (pytest)
- Migrar SQLite -> PostgreSQL
- Agendar com cron ou Airflow
