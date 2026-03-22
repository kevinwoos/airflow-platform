from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from common.dag_defaults import DEFAULT_ARGS, COMMON_TAGS


def create_k8s_job_dag(
    dag_id: str,
    schedule: str,
    image: str,
    cmds: list[str],
    arguments: list[str],
    namespace: str = "airflow",
    tags: list[str] | None = None,
):
    with DAG(
        dag_id=dag_id,
        schedule=schedule,
        default_args=DEFAULT_ARGS,
        catchup=False,
        tags=COMMON_TAGS + (tags or []),
    ) as dag:

        KubernetesPodOperator(
            task_id="run_container",
            name="run-container",
            namespace=namespace,
            image=image,
            cmds=cmds,
            arguments=arguments,
            get_logs=True,
            is_delete_operator_pod=True,
        )

    return dag
