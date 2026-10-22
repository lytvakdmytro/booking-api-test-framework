import pytest

from src.clients.api_client import APIClient
from src.clients.endpoints.health_client import HealthClient
from src.config import settings


@pytest.fixture(scope="session")
def api_client():
    """Provides a shared API client and closes its session after the test run"""
    base_url = settings.BASE_URL

    return APIClient(base_url=base_url, timeout=settings.TIMEOUT)


# Endpoint Clients
@pytest.fixture(scope="session")
def health_client(api_client):
    """Provides a Health client for the test session"""

    return HealthClient(api_client=api_client)
