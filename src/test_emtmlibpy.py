import unittest
import os
import emtmlibpy.emtmlibpy as emtm
from emtmlibpy.emtmlibpy import EMTMResult

SRC_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_FILES_PATH = os.path.join(SRC_DIR, 'test_files')


class TestEmtmlibpy(unittest.TestCase):

    def test_emtm_version(self):
        r = emtm.emtm_version()
        self.assertTupleEqual(r, (2, 0))

    def test_emtm_licence_present(self):
        r = emtm.emtm_licence_present()
        self.assertTrue(r)

    def test_em_load_data(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        self.assertIs(EMTMResult(r), EMTMResult(0))

    def test_em_clear_data(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        self.assertIs(EMTMResult(r), EMTMResult(0))

        emtm.em_clear_data()

    def test_em_op_code(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        self.assertIs(EMTMResult(r), EMTMResult(0))

        r = emtm.em_op_code()
        print(r)
        self.assertEqual(r, b'Test')




