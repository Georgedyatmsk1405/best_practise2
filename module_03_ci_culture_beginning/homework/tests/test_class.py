import unittest
import datetime
from python_advanced.module_03_ci_culture_beginning.homework.person import Person

vova=Person('vova',2000,'moskva')
class TestMaxNumberApp(unittest.TestCase):
    def test_person(self):
        date=datetime.datetime.now()
        self.assertEqual(vova.get_age(),date.year-vova.yob)
        self.assertEqual(vova.name, vova.get_name())
        newname='vladimir'
        vova.set_name(newname)
        self.assertEqual(vova.name,newname)
        newadres = 'piter'
        vova.set_address(newadres)

        self.assertEqual(vova.address, newadres)
        self.assertEqual(vova.address, vova.get_address())
        self.assertEqual(False, vova.is_homeless())



if __name__ == '__main__':
    unittest.main()