import unittest
import io
import sys
import traceback

from module_05_processes_and_threads.homework.bloc2_2 import IgnoreExceptions
class Test_ignore(unittest.TestCase):
    def test_bloc2(self):
        a = 'sss'
        obj_1 = IgnoreExceptions(a)
        assert obj_1.exception == a

    def test_bloc22(self):
        a = 'sss'
        obj_1 = IgnoreExceptions(a)
        self.assertEqual(obj_1.__exit__('sss',1,1),True)
        self.assertEqual(obj_1.__exit__('ssss', 1, 1), None)

    def test_raises_not_listed_error(self):
        with self.assertRaises(TypeError):
            with IgnoreExceptions((ZeroDivisionError,)):
                1 + '1'




if __name__ == '__main__':
            unittest.main()
