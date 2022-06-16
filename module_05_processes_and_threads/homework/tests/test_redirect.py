import unittest
import io
import sys
import traceback
from module_05_processes_and_threads.homework.bloc3_1 import RedirectFlows
from module_05_processes_and_threads.homework.bloc2_2 import IgnoreExceptions
class Test_Context(unittest.TestCase):


    def test_bloc3(self):
        a=io.StringIO()
        obj_1 = RedirectFlows(a)
        assert obj_1.st_out == a


    def test_bloc33(self):
        a = io.StringIO()
        b=RedirectFlows(a)
        c='sssss'
        with b:
            c
            self.assertEqual(sys.stdout, b.st_out)
            self.assertEqual(sys.stderr, b.er_out)

        self.assertEqual(sys.stdout, b.standart_out)
        self.assertEqual(sys.stderr, b.standart_err)

    def test_raises_redirect(self):
        with self.assertRaises(TypeError):
            with RedirectFlows(io.StringIO()):
                1 + '1'








if __name__ == '__main__':
            unittest.main()

