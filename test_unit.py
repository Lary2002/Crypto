#coding:utf8

import unittest

from src.cryptographie import chiffreletter
class TestChiffrement(unittest.TestCase):
    def test_chiffrelettre_function(self):
        a = chiffreletter('B', 'C')
        b = chiffreletter('C', 'K')
        c = chiffreletter('A', 'Z')
        d = chiffreletter('D', 'B')
        self.assertEqual(a, 'D')
        self.assertEqual(b, 'M')
        self.assertEqual(c, 'Z')
        self.assertEqual(d, 'E')


        
if __name__=='__main__':
    unittest.main()
