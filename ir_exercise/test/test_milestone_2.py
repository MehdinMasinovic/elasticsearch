import unittest

from ir_exercise.test.utils import send_request


class DivingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "dive in sea resort"
        self.gold = "The Red Sea Diving Resort"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class MissionImpossibleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Mission Impossible 3"
        self.gold = "Mission: Impossible III"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class TwentyOneTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "21"
        self.gold = "21 (2008 film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class UpgradeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "failed suicide attempt leads to STEM implant"
        self.gold = "Upgrade (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class CheTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "biography featuring Edgar Ramirez, Demian Bichir"
        self.gold = "Che (2008 film)"

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

