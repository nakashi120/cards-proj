from src.cards.api import Card


def test_equality_fail():
    c1 = Card("sit there", "Brian")
    c2 = Card("do something", "Ken")
    assert c1 == c2


if __name__ == "__main__":
    test_equality_fail()