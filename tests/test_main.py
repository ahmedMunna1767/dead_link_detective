import unittest

from detective import __main__ as main


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.main(), "Detective is running!")
