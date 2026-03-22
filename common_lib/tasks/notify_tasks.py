from common_lib.utils.log_util import get_logger

logger = get_logger(__name__)


def notify_success(dag_id: str, task_id: str) -> None:
    logger.info("[SUCCESS] dag_id=%s task_id=%s", dag_id, task_id)


def notify_failure(dag_id: str, task_id: str, message: str) -> None:
    logger.error("[FAILURE] dag_id=%s task_id=%s message=%s", dag_id, task_id, message)
