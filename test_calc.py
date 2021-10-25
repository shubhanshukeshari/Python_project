
import unittest
import main

class TestCalc(unittest.TestCase):
    def test_add(self):
        result= main.add(10,5)
        self.assertEqual(15,result)
    def test_sub(self):
        result = main.substract(10,5)
        self.assertEqual(5,result)
    
if __name__=='__main__':
    unittest.main()
