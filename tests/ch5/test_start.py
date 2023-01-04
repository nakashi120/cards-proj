from cards import Card
import pytest


def test_start_from_done(cards_db):
    index = cards_db.add_card(Card("finished item", state="done"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_in_prog(cards_db):
    index = cards_db.add_card(Card("in prog item", state="in prog"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


def test_start_from_todo(cards_db):
    index = cards_db.add_card(Card("todo item", state="todo"))
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"


@pytest.fixture(params=["done", "in prog", "todo"])
def start_state(request):
    return request.param


def test_start(cards_db, start_state):
    c = Card("write a book", state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == "in prog"
