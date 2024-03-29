import pytest

from cards import Card


@pytest.mark.smoke
def test_start(cards_db):
    """
    start changes state from "todo" to "in prog"
    :param cards_db:
    :return:
    """
    i = cards_db.add_card(Card("foo", state="todo"))
    cards_db.start(i)
    c = cards_db.get_card(i)
    assert c.state == "in prog"
