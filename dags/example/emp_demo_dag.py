from pathlib import Path
from airflow.sdk import task

from common.base_dag import build_demo_dag
from common.db.postgres_tasks import build_postgres_sql_task
from common.db.postgres_helper import select_emp_rows, assert_rows_exist

DAG_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = DAG_DIR.parent / "templates"

with build_demo_dag(
    dag_id="sample_emp_demo",
    tags=["postgres", "sample", "emp"],
    schedule=None,
    template_searchpath=[str(TEMPLATE_DIR)],
) as dag:

    create_emp_table = build_postgres_sql_task(
        task_id="create_emp_table",
        sql="sql/emp_create.sql",
    )

    insert_emp_rows = build_postgres_sql_task(
        task_id="insert_emp_rows",
        sql="sql/emp_insert.sql",
    )

    @task(task_id="select_emp_rows")
    def select_emp_rows_task():
        rows = select_emp_rows("sql/emp_select.sql")
        rows = assert_rows_exist(rows)

        for row in rows:
            print(row)

        return [list(row) for row in rows]

    create_emp_table >> insert_emp_rows >> select_emp_rows_task()