from common_lib.utils.log_util import get_logger

logger = get_logger(__name__)


class DbClient:
    def __init__(self, dsn: str):
        self.dsn = dsn

    def query_one(self, sql: str) -> dict:
        logger.info("query_one sql=%s dsn=%s", sql, self.dsn)
        return {"status": "ok", "row_count": 1}
