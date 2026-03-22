from airflow.decorators import task

from dags.common.dag.base_dag import build_demo_dag
from dags.common.db.postgres_tasks import build_postgres_sql_task
from dags.common.db.postgres_helper import select_emp_rows, assert_rows_exist


with build_demo_dag(
    dag_id="sample_emp_demo",
    tags=["postgres", "sample", "emp"],
    schedule=None,
) as dag:

    create_emp_table = build_postgres_sql_task(
        task_id="create_emp_table",
        sql="templates/sql/emp_create.sql",
    )

    insert_emp_rows = build_postgres_sql_task(
        task_id="insert_emp_rows",
        sql="templates/sql/emp_insert.sql",
    )

    @task(task_id="select_emp_rows")
    def select_emp_rows_task():
        rows = select_emp_rows("templates/sql/emp_select.sql")
        rows = assert_rows_exist(rows)

        for row in rows:
            print(row)

        return [list(row) for row in rows]

    create_emp_table >> insert_emp_rows >> select_emp_rows_task()