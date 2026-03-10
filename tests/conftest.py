from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


# Snapshot initial state once; each test gets a deep-copied reset.
_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client() -> TestClient:
    return TestClient(app_module.app)
