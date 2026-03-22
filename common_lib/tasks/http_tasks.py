from common_lib.clients.http_client import HttpClient


def invoke_api(endpoint: str, method: str = "POST", payload: dict | None = None) -> dict:
    client = HttpClient(timeout=30)
    return client.request(method=method, url=endpoint, json_payload=payload or {})
