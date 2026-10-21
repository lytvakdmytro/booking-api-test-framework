from src.clients.api_client import APIClient


class BaseEndpointClient:
    """Base class for endpoint clients"""

    def __init__(self, api_client: APIClient):
        """Initializes endpoint client with the shared API client"""
        self._api = api_client
