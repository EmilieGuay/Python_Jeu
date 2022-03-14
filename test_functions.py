import unittest

class Samples(unittest.TestCase):
    def test(self):
        self.assertEqual(cubeA(3), 27)
        self.assertRaises(TypeError, cubeA, "s")
        
