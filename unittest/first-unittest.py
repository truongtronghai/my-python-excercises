import unittest

class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('bar'.isupper())

    def test_split(self):
        self.assertEqual("hello world".split(),["hello","world"])

        with self.assertRaises(TypeError):
            "hello world".split(2) # test with seperator is 2

if __name__ == '__main__':
    unittest.main()