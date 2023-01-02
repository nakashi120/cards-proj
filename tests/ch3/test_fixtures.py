import pytest


@pytest.fixture()
def some_data():
    """Return answer to ultimate question."""
    return 42


@pytest.fixture()
def new_dict():
    """Return sample dictionaly."""
    return {"id": 100, "name": "Ken"}


def test_some_data(some_data):
    """Use fixture return value in assert"""
    assert some_data == 42


def test_new_dict(new_dict):
    assert new_dict == {
        "id": 100,
        "name": "Ken",
    }