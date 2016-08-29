import unittest
import DICT as test

class Test_DICT(unittest.TestCase):
    def test_default_case(self):
        self.assertEqual(test.solve(5, 2, 11), 'abaaaab')
        self.assertEqual(test.solve(5, 6, 17), 'aaabbabbbab')
        self.assertEqual(test.solve(1, 1, 2), 'ba')
        self.assertEqual(test.solve(4, 0, 2), 'NONE')

    def test_zero_case(self):
        self.assertEqual(test.solve(0, 0, 2), 'NONE')
        self.assertEqual(test.solve(0, 0, 1), 'NONE')
        self.assertEqual(test.solve(0, 1, 1), 'b')
        self.assertEqual(test.solve(1, 0, 1), 'a')

    def test_maximum_case(self):
        self.assertEqual(test.solve(1, 1, 2), 'ba')
        self.assertEqual(test.solve(5, 2, 21), 'bbaaaaa')
        self.assertEqual(test.solve(10, 10, 184756), 'bbbbbbbbbbaaaaaaaaaa')
        self.assertEqual(test.solve(100, 100, 100000000),
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbabbbbbbbbbbbbbbbbbbbbbbbbbbbba')

    def test_exceed_case(self):
        self.assertEqual(test.solve(1, 1, 3), 'NONE')
        self.assertEqual(test.solve(2, 1, 4), 'NONE')
        self.assertEqual(test.solve(5, 5, 253), 'NONE')


if __name__ == "__main__":
    unittest.main()
