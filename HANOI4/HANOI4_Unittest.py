test = __import__('HANOI4_Bit')
import unittest
import random

class Test_HANOI4(unittest.TestCase):
    def test_exam1(self):
        num = 5
        state = test.set_list(0, [1],0)
        state = test.set_list(state, [3],1)
        state = test.set_list(state, [5,4],2)
        state = test.set_list(state, [2],3)
        self.assertEqual(test.solve(num, state),  10)

    def test_exam2(self):
        num = 3
        state = test.set_list(0, [2],0)
        state = test.set_list(state, [3,1],2)
        self.assertEqual(test.solve(num, state),  4)

    def test_exam3(self):
        num = 10
        state = test.set_list(0, [8,7],0)
        state = test.set_list(state, [5,4],1)
        state = test.set_list(state, [6,3,2],2)
        state = test.set_list(state, [10,9,1],3)
        for _ in xrange(50):
            test.solve(num, state)
        self.assertEqual(test.solve(num, state),  24)



if __name__ == "__main__":
    unittest.main()
