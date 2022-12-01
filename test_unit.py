#coding:utf8

import unittest

from src.cryptographie import chiffreletter
class TestChiffrement(unittest.TestCase):
    def test_chiffrelettre_function(self):
        a = chiffreletter('B', 'C')
        self.assertEqual(a, 'D')


        
if __name__=='__main__':
    unittest.main()
