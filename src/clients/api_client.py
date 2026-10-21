import requests


class APIClient:
    """Base HTTP client for interacting with the API"""

    def __init__(self, base_url: str):
        """Initializes API client"""

        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def request(
        self,
        method: str,
        endpoint: str,
        headers: dict | None = None,
        json: dict | None = None,
        params: dict | None = None,
        **kwargs,
    ):
        """Creates and executes a request to the API"""

        full_url = f"{self.base_url}{endpoint}"

        response = self.session.request(
            method=method,
            url=full_url,
            headers=headers,
            json=json,
            params=params,
            **kwargs,
        )
        return response
