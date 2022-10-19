import unittest


addtwo = lambda x: x+2


class LamdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # should fail
        self.assertEqual(addtwo(3), 6)


# checking whether app runs as a single file ( not imported module )
if __name__ == '__main__':
    unittest.main(verbosity=2)
