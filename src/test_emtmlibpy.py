import unittest
import os
import emtmlibpy.emtmlibpy as emtm
from emtmlibpy.emtmlibpy import Result

SRC_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_FILES_PATH = os.path.join(SRC_DIR, 'test_files')


class TestEmtmlibpy(unittest.TestCase):

    def test_emtm_version(self):
        r = emtm.emtm_version()
        self.assertTupleEqual(r, (2, 0))
