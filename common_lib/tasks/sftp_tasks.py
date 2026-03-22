from common_lib.clients.sftp_client import SftpClient, SftpConnectionInfo


def run_sftp_transfer(source_path: str, target_path: str) -> dict:
    conn = SftpConnectionInfo(
        host="sftp.internal.local",
        port=22,
        username="airflow",
        password=None,
    )
    client = SftpClient(conn)
    client.download(source_path, "/tmp/input.dat")
    client.upload("/tmp/input.dat", target_path)

    return {
        "source_path": source_path,
        "target_path": target_path,
        "status": "success",
    }
