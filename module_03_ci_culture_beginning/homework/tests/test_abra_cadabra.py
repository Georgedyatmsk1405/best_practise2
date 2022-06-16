import unittest
from python_advanced.module_03_ci_culture_beginning.homework.decrypt import decrypt



class Testdecrypt(unittest.TestCase):
    def test_decrypt(self):
        self.assertEqual(decrypt('абра-кадабра.'),'абра-кадабра')
        self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')
        self.assertEqual(decrypt('абра........'), '')
        self.assertEqual(decrypt('абр......а'), 'а')
        self.assertEqual(decrypt('1..2.3'), '23')
        self.assertEqual(decrypt('.'), '')
        self.assertEqual(decrypt('1.......................'), '')



if __name__ == '__main__':
    unittest.main()


