from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import os

def check_sftp_directory():
    path = "/app/data/sftp/"

    if os.path.exists(path):
        print("True")
        return True
    else:
        print("False")
        return False


with DAG(
    dag_id="check_sftp_path_exists",
    start_date=datetime(2026, 3, 21),
    schedule="*/5 * * * *",  # 매시간 정각
    catchup=False,
    tags=["sftp", "check"],
    max_active_runs=1,
    max_active_tasks=5,  # task가 병렬로 최대 5
) as dag:

    check_task = PythonOperator(
        task_id="check_path",
        python_callable=check_sftp_directory,
    )
