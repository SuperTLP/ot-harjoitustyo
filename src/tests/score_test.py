from repositories.score import Score
import unittest
from unittest import mock

class TestScore(unittest.TestCase):
    def setUp(self):

        self.cursor = mock.MagicMock()
        self.cursor.execute=mock.MagicMock()

        self.db=mock.MagicMock()
        self.db.cursor=mock.MagicMock(return_value=self.cursor)
        self.db.commit=mock.MagicMock()

    def test_new_score(self):
        score = Score(self.db)
        score.new("tester", 20, "easy")
        self.db.cursor.assert_called()
        self.cursor.execute.assert_called_with("insert into scores (name, score, difficulty) values (?, ?, ?)", ["tester", 20, "easy"])
        self.db.commit.assert_called()
