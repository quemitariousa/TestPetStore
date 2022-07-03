import pytest

from api.client.api_client import ApiClient


@pytest.fixture(scope="function")
def api_client() -> ApiClient:
    URL = 'http://petstore.swagger.io/v2'
    api_client = ApiClient(base_url=URL)
    return api_client
