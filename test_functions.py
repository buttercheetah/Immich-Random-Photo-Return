import unittest
import os
import random
import string
import functions

class TestFunctions(unittest.TestCase):

    def test_getimages(self):
        cwd = os.getcwd()
        print(cwd)
        tmpdir = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=7))
        os.mkdir(tmpdir)
        with open(f'{tmpdir}/1.png', 'w') as fp:
            pass
        with open(f'{tmpdir}/2.jpg', 'w') as fp:
            pass
        result1 = functions.getimages(f'{cwd}/{tmpdir}','png')
        self.assertEqual(result1, ['1.png'])
        result2 = functions.getimages(f'{cwd}/{tmpdir}','jpg')
        self.assertEqual(result2, ['2.jpg'])
        os.chdir(cwd)
        os.remove(f'{cwd}/{tmpdir}/1.png')
        os.remove(f'{cwd}/{tmpdir}/2.jpg')
        os.rmdir(f'{cwd}/{tmpdir}')
