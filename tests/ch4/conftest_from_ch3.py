from pathlib import Path
from tempfile import TemporaryDirectory
import pytest
import cards


@pytest.fixture()
def db():
    """CardsDB object connected to a temporary database."""
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        db_ = cards.CardsDB(db_path)
        yield db_
        db_.close()
