import unittest

from ir_exercise.test.utils import send_request


class TroyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Brad Pitt in Ancient Greece"
        self.gold = "Troy (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class CastAwayTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Academy Award winning Tom Hangs on uninhabted island"
        self.gold = "Cast Away"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class OverTheHedgeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "RJ the racoon steals snack food"
        self.gold = "Over the Hedge (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class BeethovenTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "2001 family comedy featuring St. Bernard"
        self.gold = "Beethoven's 4th (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class RoyalChristmasTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Royal Ch"
        self.gold = "A Royal Christmas"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


if __name__ == "__main__":
    unittest.main()

