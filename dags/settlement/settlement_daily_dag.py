from dags.templates.api_template import create_api_dag

dag = create_api_dag(
    dag_id="settlement_daily_api",
    schedule="30 1 * * *",
    endpoint="http://batch-api.batch.svc.cluster.local/jobs/settlement/run",
    method="POST",
    payload={"job_name": "settlementDaily"},
    tags=["settlement", "api"],
)
