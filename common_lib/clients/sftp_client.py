from dataclasses import dataclass
from common_lib.utils.log_util import get_logger

logger = get_logger(__name__)


@dataclass
class SftpConnectionInfo:
    host: str
    port: int
    username: str
    password: str | None = None


class SftpClient:
    def __init__(self, conn: SftpConnectionInfo):
        self.conn = conn

    def download(self, remote_path: str, local_path: str) -> None:
        logger.info(
            "download remote_path=%s local_path=%s host=%s",
            remote_path, local_path, self.conn.host
        )

    def upload(self, local_path: str, remote_path: str) -> None:
        logger.info(
            "upload local_path=%s remote_path=%s host=%s",
            local_path, remote_path, self.conn.host
        )
