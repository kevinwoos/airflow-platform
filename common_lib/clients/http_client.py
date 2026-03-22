import requests


class HttpClient:
    def __init__(self, timeout: int = 30):
        self.timeout = timeout

    def request(self, method: str, url: str, json_payload: dict | None = None) -> dict:
        response = requests.request(
            method=method,
            url=url,
            json=json_payload or {},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return {
            "status_code": response.status_code,
            "text": response.text,
        }
