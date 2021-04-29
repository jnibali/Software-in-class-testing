import unittest
import calculator

class testCaseAdd(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(calculator.runCalculator(3,4),7)
        self.assertEqual(calculator.runCalculator(4,3),1)
        self.assertEqual(calculator.runCalculator(5,5),25)
        self.assertEqual(calculator.runCalculator(5,5),1)

#tests for additon, then subtraction, then multiply, and then division
#select right options in terminal when testing

if __name__ == '__main__':
    unittest.main()