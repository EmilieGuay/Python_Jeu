def square34(number):
    return number*number



import unittest
class Samples(unittest.TestCase):
    def test(self):
        self.assertEqual(square34(3), 9)

        
