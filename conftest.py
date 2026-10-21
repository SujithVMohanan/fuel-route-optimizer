from collections.abc import Callable
from typing import Any

import pytest
from django.core.cache import cache  # type: ignore[import-untyped]
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def _fast_settings(settings: Any) -> None:
    settings.PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
    settings.AUTH_THROTTLE_DISABLED = True
    cache.clear()


@pytest.fixture
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture
def client_for() -> Callable[[Any], APIClient]:
    def _client(user: Any) -> APIClient:
        client = APIClient()
        client.force_authenticate(user)
        return client

    return _client
