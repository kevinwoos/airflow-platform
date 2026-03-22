from templates.sftp_template import create_sftp_dag

dag = create_sftp_dag(
    dag_id="sales_daily_sftp",
    schedule="0 2 * * *",
    source_path="/inbound/sales",
    target_path="/archive/sales",
    tags=["sales", "sftp"],
)
