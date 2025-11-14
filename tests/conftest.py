"""General test helper, which are available for all tests."""

import pytest
from unittest.mock import patch

from src.service import Service


@pytest.fixture
def patched_api_url():
    """Fixture to patch the API_URL to a known value for service usage(showcase for constant mocking)."""
    with patch("src.service.API_URL", "https://mocked.com"):
        # Although API_URL is defined in config we have to patch it in service
        #  Due to import order service.py has a copy of the original API_URL before it got patched
        #  and therefore has no effect
        yield  # !yield is used to profit from the patched url, but after usage the patch is rolled back!


@pytest.fixture(params=[(2, 3, 5), (10, -5, 5), (0, 0, 0)])
def addition_cases(request):
    """Parametrized fixture for addition cases."""
    return request.param


@pytest.fixture
def sample_service():
    """Some reusable service definition."""
    return Service()