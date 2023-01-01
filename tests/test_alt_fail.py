import pytest
from src.cards.api import Card


def test_with_fail():
    c1 = Card("sit there", "Brian")
    c2 = Card("do something", "Ken")
    if c1 != c2:
        pytest.fail("They don't match")
