from datetime import datetime
from airflow.sdk import DAG

def build_demo_dag(
    dag_id: str,
    tags: list[str] | None = None,
    schedule=None,
    template_searchpath: list[str] | None = None,
):
    return DAG(
        dag_id=dag_id,
        start_date=datetime(2024, 1, 1),
        schedule=schedule,
        catchup=False,
        tags=["demo"] + (tags or []),
        template_searchpath=template_searchpath or [],
    )