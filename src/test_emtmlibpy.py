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
        self.assertEqual(r, b'Test')

    def test_em_units(self):
        r = emtm.em_units()
        self.assertEqual(r, b'mm')

    def test_em_unique_fgs(self):
        r = emtm.em_unique_fgs()
        self.assertEqual(r, 6)

    def test_get_unique_fgs(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        fgs = [(b'', b'', b''),
               (b'balistidae', b'abalistes', b'stellatus'),
               (b'nemipteridae', b'nemipterus', b'furcosus'),
               (b'nemipteridae', b'pentapodus', b'porosus'),
               (b'pinguipedidae', b'parapercis', b'xanthozona'),
               (b'scombridae', b'scomberomorus', b'queenslandicus')]

        n_unique = emtm.em_unique_fgs()

        for ii in range(n_unique):
            r = emtm.em_get_unique_fgs(ii)
            self.assertTupleEqual(r, fgs[ii])

    def test_em_measurement_count_fgs(self):

        r = emtm.em_measurement_count_fgs('balistidae', 'abalistes', 'stellatus')
        print(r)

