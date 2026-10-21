import pytest

from src.clients.api_client import APIClient
from src.clients.endpoints.health_client import HealthClient
from src.config import settings


@pytest.fixture(scope="session")
def api_client():
    """Initialize API client"""
    base_url = settings.BASE_URL

    return APIClient(base_url=base_url)


# Endpoint Clients
@pytest.fixture(scope="session")
def health_client(api_client):
    """Initialize Health client"""

    return HealthClient(api_client=api_client)
