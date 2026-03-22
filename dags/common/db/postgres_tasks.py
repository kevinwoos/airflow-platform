from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from common.db.postgres_config import EMP_DB_CONN_ID


def build_postgres_sql_task(
    task_id: str,
    sql: str,
    parameters: dict | None = None,
    autocommit: bool = True,
):
    return SQLExecuteQueryOperator(
        task_id=task_id,
        conn_id=EMP_DB_CONN_ID,
        sql=sql,
        parameters=parameters or {},
        autocommit=autocommit,
    )