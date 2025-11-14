"""Tests for service class."""

from unittest.mock import MagicMock, patch
from test_exampels import service as sv


def test_mock_function():
    """Test using patch to replace a method call requests.get with a MagicMock with in a method of a class."""
    with patch("test_exampels.service.requests.get") as mock_get:
        mock_response = MagicMock()
        # return_value is what will be returned when called
        #  here: print(
        mock_response.json.return_value = {"status": "ok"}
        mock_get.return_value = mock_response

        service = sv.Service()
        result = service.fetch_data("test")

        assert result == {"status": "ok"}
        mock_get.assert_called_once_with("https://example.com/api/test", timeout=5)


def test_mock_class():
    """Test to mock a method of the Service class directly."""
    with patch("test_exampels.service.Service") as MockService:
        instance = MockService.return_value
        instance.fetch_data.return_value = {"fake": True}

        fake = sv.Service()
        assert fake.fetch_data("anything") == {"fake": True}
        # asserts if method/function is called not or more than one time
        instance.fetch_data.assert_called_once()


def test_mock_method(sample_service):
    """Test to mock a method on an instance."""
    with patch.object(sample_service, "multiply", return_value=42) as mock_method:
        assert sample_service.multiply(2, 3) == 42
        # asserts if method/function is not called with given parameters
        mock_method.assert_called_once_with(2, 3)


def test_mock_attribute(sample_service):
    """Test to mock an attribute on an instance."""
    with patch.object(sample_service, "base_url", "https://patched.com"):
        assert sample_service.base_url == "https://patched.com"


def test_fetch_data_uses_patched_url(patched_api_url):
    """Test where a constant got mocked."""
    with patch("test_exampels.service.requests.get") as mock_get:
        # patch requests.get to check later if it got called with mocked URL (just for demonstration)
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_get.return_value = mock_response

        service = sv.Service()
        result = service.fetch_data("endpoint")

        assert result == {"status": "ok"}

        # just a check if url got mocked (usually it is not tested if mocking succeeded)
        mock_get.assert_called_once_with("https://mocked.com/endpoint", timeout=5)
