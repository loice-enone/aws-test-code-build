import unittest
from app import say_hello

class testapp(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("aws"), "hello, aws")
        
if __nme== "__main__":
    unittest.main()
