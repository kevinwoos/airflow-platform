from pathlib import Path
import yaml
from templates.sftp_template import create_sftp_dag

CONFIG_DIR = Path("/opt/airflow/dags/configs/dev")

for config_file in CONFIG_DIR.glob("*.yaml"):
    conf = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    dag_id = conf["dag_id"]

    globals()[dag_id] = create_sftp_dag(
        dag_id=dag_id,
        schedule=conf["schedule"],
        source_path=conf["source_path"],
        target_path=conf["target_path"],
        tags=conf.get("tags", []),
    )
