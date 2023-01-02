from src.cards import Card


class TestEquality:
    def test_equality(self):
        # GIVEN
        c1 = Card("something", "Brian", "todo", 123)
        c2 = Card("something", "Brian", "todo", 123)

        # THEN
        assert c1 == c2

    def test_equality_with_diff_ids(self):
        c1 = Card("something", "Brian", "todo", 123)
        c2 = Card("something", "Brian", "todo", 4567)

        assert c1 == c2

    def test_inequality(self):
        c1 = Card("something", "Brian", "todo", 123)
        c2 = Card("Completely different", "Ken", "done", 123)

        assert c1 != c2
