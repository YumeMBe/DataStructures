import unittest
import random
import time

from LinkedListSingle import LinkedList


class TestSingleLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.lista = LinkedList([3, 9, 0, 17, 2])

    def test_insert(self):
        self.lista.insert(20)
        self.assertEqual(self.lista.length_list(), 6)

    def test_delete(self):
        self.lista.delete(9)
        self.assertEqual(self.lista.length_list(), 4)

    def test_search(self):
        cautatura = self.lista.search(17)
        self.assertNotEqual(cautatura, None)

class RunningTime(unittest.TestCase):
    def setUp(self) -> None:
        self.random_list = [random.randint(0, 100000) for _ in range(10000)]

    def test_time_creation(self):
        lista_timpulamea = []

        for _ in range(100):
            timpulamea = self.get_duration()
            lista_timpulamea.append(timpulamea)
        avg_timpulamea = sum(lista_timpulamea) / len(lista_timpulamea)
        print(avg_timpulamea)

    def get_duration(self):
        time_start = time.time()
        cur = LinkedList(self.random_list)
        duration = time.time() - time_start
        return duration
