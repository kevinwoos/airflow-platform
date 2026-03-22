from airflow import DAG
from airflow.decorators import task
from common.dag_defaults import DEFAULT_ARGS, COMMON_TAGS
from common.callbacks import on_failure_callback


def create_sftp_dag(
    dag_id: str,
    schedule: str,
    source_path: str,
    target_path: str,
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

        @task(task_id="precheck")
        def precheck():
            return {
                "source_path": source_path,
                "target_path": target_path,
            }

        @task(task_id="transfer")
        def transfer(ctx: dict):
            from common_lib.tasks.sftp_tasks import run_sftp_transfer
            return run_sftp_transfer(ctx["source_path"], ctx["target_path"])

        @task(task_id="notify")
        def notify(result: dict):
            from common_lib.tasks.notify_tasks import notify_success
            notify_success(dag_id, "notify")
            return result

        ctx = precheck()
        result = transfer(ctx)
        notify(result)

    return dag
