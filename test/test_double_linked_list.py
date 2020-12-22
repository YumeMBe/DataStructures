import unittest

from DoubleLinkedList import DoubleLinked


class DoubleLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.lstdoublelinked = DoubleLinked([6, 9, 4, 7, 45, 23, 16])

    def test_creation(self):
        self.assertEqual(7, self.lstdoublelinked.lst_length())

    def test_insert(self):
        self.lstdoublelinked.insert_elm(35)
        self.assertEqual(8, self.lstdoublelinked.lst_length())

    def test_delete(self):
        self.lstdoublelinked.delete_elm(7)
        self.assertEqual(self.lstdoublelinked.lst_length(), 6)

    def test_search(self):
        cautatura = self.lstdoublelinked.search_elm(23)
        self.assertNotEqual(cautatura, None)

