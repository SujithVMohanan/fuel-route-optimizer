from collections.abc import Generator
from contextlib import contextmanager
from datetime import UTC, datetime

import pytest
from rest_framework.exceptions import APIException

NOW = datetime(2026, 2, 10, 12, 0, tzinfo=UTC)
TODAY = NOW.date()


@contextmanager
def raises_code(code: str) -> Generator[pytest.ExceptionInfo[APIException], None, None]:
    with pytest.raises(APIException) as info:
        yield info
    assert getattr(info.value, "error_code", None) == code, info.value
