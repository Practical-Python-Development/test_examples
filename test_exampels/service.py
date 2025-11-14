"""Sample service class to showcase some test options."""

from typing import Any

import requests

from test_exampels.config import API_URL, TIMEOUT


class Service:
    """Important service."""

    def __init__(self):
        """Initialization of a service."""
        self.base_url = API_URL

    def fetch_data(self, endpoint: str) -> Any:
        """
        Fetch data from endpoint.

        :param endpoint: from which to fetch data.
        :return: response as JSON structure.
        """
        response = requests.get(f"{self.base_url}/{endpoint}", timeout=TIMEOUT)
        return response.json()

    @staticmethod
    def multiply(a: int, b: int) -> int:
        """Multiply two integers."""
        return a * b
