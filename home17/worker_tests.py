import unittest
from worker_boss_class import Person, Worker, Boss


class TestWorker(unittest.TestCase):

    def setUp(self) -> None:
        self.boss1 = Boss(1234, "Robert", "Apple")
        self.boss2 = Boss(1234, "Peter", "Google")
        self.worker1 = Worker(1111, "Steve", "Apple", self.boss1)
        self.worker2 = Worker(1111, "Steve", "Apple", self.boss1)

    def test_company_change(self):
        self.worker1.boss = self.boss2
        self.assertEqual(self.worker1.company, "Google")
        self.assertEqual(self.worker2.company, "Apple")

    def test_worker_boss_is_class(self):
        self.assertIsInstance(self.worker1.boss, Boss)

    def test_repr(self):
        self.assertEqual(repr(self.worker1), "Steve 1111 Apple")

