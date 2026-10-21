from src.clients.base_endpoint_client import BaseEndpointClient


class HealthClient(BaseEndpointClient):
    """Client for the Health endpoint"""

    HEALTH_PATH = "/ping"

    def check_health(self):
        """Sends a health check request to the API"""

        return self._api.request(
            method="GET",
            endpoint=self.HEALTH_PATH,
        )
