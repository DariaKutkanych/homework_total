import unittest
from worker_boss_class import Person, Worker, Boss


class TestBoss(unittest.TestCase):

    def setUp(self) -> None:
        self.boss1 = Boss(1234, "Robert", "Apple")
        self.boss2 = Boss(1234, "Peter", "Google")
        self.worker1 = Worker(1111, "Steve", "Apple", self.boss1)
        self.worker2 = Worker(1111, "Steve", "Apple", self.boss1)

    def test_boss_worker_change(self):
        self.worker1.boss = self.boss2
        self.assertEqual(len(self.boss1.workers), 1)
        self.assertEqual(len(self.boss2.workers), 1)

    def test_repr(self):
        self.assertEqual(repr(self.boss1), "Robert 1234 Apple")

    def test_workers_objects(self):
        self.assertIsInstance(self.boss1.workers[0], Worker)



