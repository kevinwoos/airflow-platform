from datetime import timedelta

DEFAULT_ARGS = {
    "owner": "data-platform",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

COMMON_TAGS = ["aks", "airflow", "standard"]
