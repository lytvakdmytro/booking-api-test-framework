class TestHealth:
    """Tests for the Health endpoint"""

    def test_health(self, health_client):
        """Verifies that the health endpoint is working"""

        response = health_client.check_health()

        assert response.status_code == 201
