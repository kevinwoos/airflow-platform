from airflow.models import BaseOperator
from airflow.utils.context import Context


class BatchApiOperator(BaseOperator):
    template_fields = ("endpoint", "payload")

    def __init__(self, endpoint: str, payload: dict | None = None, **kwargs):
        super().__init__(**kwargs)
        self.endpoint = endpoint
        self.payload = payload or {}

    def execute(self, context: Context):
        self.log.info("Invoke endpoint: %s", self.endpoint)
        self.log.info("Payload: %s", self.payload)
        return {
            "status": "success",
            "endpoint": self.endpoint,
        }
