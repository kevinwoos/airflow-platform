from airflow import DAG
from airflow.decorators import task
from dags.common.dag_defaults import DEFAULT_ARGS, COMMON_TAGS
from dags.common.callbacks import on_failure_callback


def create_api_dag(
    dag_id: str,
    schedule: str,
    endpoint: str,
    method: str = "POST",
    payload: dict | None = None,
    tags: list[str] | None = None,
):
    with DAG(
        dag_id=dag_id,
        schedule=schedule,
        default_args=DEFAULT_ARGS,
        catchup=False,
        tags=COMMON_TAGS + (tags or []),
        on_failure_callback=on_failure_callback,
    ) as dag:

        @task(task_id="invoke_api")
        def invoke():
            from common_lib.tasks.http_tasks import invoke_api
            return invoke_api(endpoint=endpoint, method=method, payload=payload or {})

        @task(task_id="notify")
        def notify(result: dict):
            from common_lib.tasks.notify_tasks import notify_success
            notify_success(dag_id, "notify")
            return result

        result = invoke()
        notify(result)

    return dag
