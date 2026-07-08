import pytest
from src.clients.user_client import UserClient


@pytest.fixture
def user_client():
    """Provides a reusable instance of UserClient to tests."""
    client = UserClient()
    yield client
