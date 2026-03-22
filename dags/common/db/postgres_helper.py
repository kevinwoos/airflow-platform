from pathlib import Path
from airflow.providers.postgres.hooks.postgres import PostgresHook
from common.db.postgres_config import EMP_DB_CONN_ID

BASE_DIR = Path(__file__).resolve().parents[2]

def load_sql(relative_path: str) -> str:
    sql_path = BASE_DIR / relative_path
    return sql_path.read_text(encoding="utf-8")


def select_records_from_sql_file(relative_path: str, parameters: dict | None = None):
    hook = PostgresHook(postgres_conn_id=EMP_DB_CONN_ID)
    sql = load_sql(relative_path)
    return hook.get_records(sql=sql, parameters=parameters or {})

def select_emp_rows(sql: str, parameters: dict | None = None):
    hook = PostgresHook(postgres_conn_id=EMP_DB_CONN_ID)
    return hook.get_records(sql=sql, parameters=parameters or {})


def assert_rows_exist(rows):
    if not rows:
        raise ValueError("조회 결과가 없음")
    return rows
