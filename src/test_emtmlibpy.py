import unittest
import os
import emtmlibpy.emtmlibpy as emtm
from emtmlibpy.emtmlibpy import EMTMResult
from collections import namedtuple

SRC_DIR = os.path.abspath(os.path.dirname(__file__))
TEST_FILES_PATH = os.path.join(SRC_DIR, 'test_files')

assert os.path.exists(TEST_FILES_PATH), f"Please ensure you place the required test files at: {TEST_FILES_PATH}"

class TestEmtmlibpy(unittest.TestCase):

    def tearDown(self) -> None:
        emtm.em_clear_data()
        emtm.tm_clear_data()

    def test_emtm_version(self):
        r = emtm.emtm_version()
        self.assertTupleEqual(r, (2, 0))

    def test_emtm_licence_present(self):
        r = emtm.emtm_licence_present()
        self.assertTrue(r)

    def test_em_load_data(self):
        self.assertRaises(emtm.EmTmError, emtm.em_load_data, "fake path")
        self.assertRaises(emtm.EmTmError, emtm.em_load_data, "/totally/fake/and/made/up/path/which/surely/doesnt/exist/on/anyones/machine")
        self.assertRaises(emtm.EmTmError, emtm.em_load_data, "")
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

    def test_em_clear_data(self):
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        emtm.em_clear_data()

    def test_em_op_code(self):
        # self.assertRaises(emtm.EmTmError, emtm.em_op_code)  # FIXME: EMOpCode() appears to return success, even if no file is loaded!
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        r = emtm.em_op_code()
        self.assertEqual(r, 'Test')

    def test_em_units(self):
        # self.assertRaises(emtm.EmTmError, emtm.em_units)  # FIXME: EMUnits() appears to return success, even if no file is loaded!
        r = emtm.em_units()
        self.assertEqual(r, 'mm')

    def test_em_unique_fgs(self):
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        r = emtm.em_unique_fgs()
        self.assertEqual(r, 6)

    def test_get_unique_fgs(self):
        self.assertRaises(emtm.EmTmError, emtm.em_get_unique_fgs, -1)
        self.assertRaises(emtm.EmTmError, emtm.em_get_unique_fgs, 0)
        self.assertRaises(emtm.EmTmError, emtm.em_get_unique_fgs, 1)
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        fgs = [('', '', ''),
               ('balistidae', 'abalistes', 'stellatus'),
               ('nemipteridae', 'nemipterus', 'furcosus'),
               ('nemipteridae', 'pentapodus', 'porosus'),
               ('pinguipedidae', 'parapercis', 'xanthozona'),
               ('scombridae', 'scomberomorus', 'queenslandicus')]

        n_unique = emtm.em_unique_fgs()

        self.assertRaises(emtm.EmTmError, emtm.em_get_unique_fgs, -1)
        for ii in range(n_unique):
            r = emtm.em_get_unique_fgs(ii)
            self.assertTupleEqual(r, fgs[ii])
        self.assertRaises(emtm.EmTmError, emtm.em_get_unique_fgs, ii + 1)

    def test_em_measurement_count_fgs(self):
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        FGS = namedtuple('FGS', 'point box xyz_point, length cpd_length')

        r = emtm.em_measurement_count_fgs('balistidae', 'abalistes', 'stellatus')
        self.assertTupleEqual(r, FGS(point=6, box=1, xyz_point=0, length=4, cpd_length=0))

        r = emtm.em_measurement_count_fgs('*', '*', '*')
        self.assertTupleEqual(r, FGS(point=31, box=4, xyz_point=2, length=21, cpd_length=1))

        r = emtm.em_measurement_count_fgs('nemipteridae', '*', '*')
        self.assertTupleEqual(r, FGS(point=14, box=2, xyz_point=1, length=14, cpd_length=0))

        r = emtm.em_measurement_count_fgs('*', '*', 'furcosus')
        self.assertTupleEqual(r, FGS(point=6, box=0, xyz_point=1, length=4, cpd_length=0))

    def test_em_point_count(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        r = emtm.em_point_count()
        PointCount = namedtuple('PointCount', 'total bbox')
        self.assertTupleEqual(r, PointCount(total=35, bbox=4))

    def test_em_get_point(self):
        self.assertRaises(emtm.EmTmError, emtm.em_get_point, -1)
        self.assertRaises(emtm.EmTmError, emtm.em_get_point, 0)
        self.assertRaises(emtm.EmTmError, emtm.em_get_point, 1)
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        point_count = emtm.em_point_count()
        p = emtm.em_get_point(0)  # just so we can get the fields

        em_point_values = []
        em_point_fields = [field[0] for field in p._fields_]

        self.assertRaises(emtm.EmTmError, emtm.em_get_point, -1)
        for ii in range(point_count.total):
            em_point_values = []
            p = emtm.em_get_point(ii)
            for fields in em_point_fields:
                em_point_values.append(p.__getattribute__(fields))
        self.assertRaises(emtm.EmTmError, emtm.em_get_point, ii + 1)

    def test_em_3d_point_count(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        r = emtm.em_3d_point_count()
        self.assertEqual(r, 2)

    def test_em_get_3d_point(self):
        self.assertRaises(emtm.EmTmError, emtm.em_get_3d_point, -1)
        self.assertRaises(emtm.EmTmError, emtm.em_get_3d_point, 0)
        self.assertRaises(emtm.EmTmError, emtm.em_get_3d_point, 1)
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        point_count = emtm.em_3d_point_count()
        p = emtm.em_get_3d_point(0)  # just so we can get the fields

        em_point_values = []
        em_point_fields = [field[0] for field in p._fields_]

        self.assertRaises(emtm.EmTmError, emtm.em_get_3d_point, -1)
        for ii in range(point_count):
            em_point_values = []
            p = emtm.em_get_3d_point(ii)
            for fields in em_point_fields:
                em_point_values.append(p.__getattribute__(fields))
        self.assertRaises(emtm.EmTmError, emtm.em_get_3d_point, ii + 1)

    def test_em_get_length_count(self):
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))

        pn_compound = emtm.em_get_length_count()
        LengthCount = namedtuple('LengthCount', 'total compound')

        self.assertTupleEqual(pn_compound, LengthCount(total=22, compound=0))

    def test_em_get_length(self):
        self.assertRaises(emtm.EmTmError, emtm.em_get_length, -1)
        self.assertRaises(emtm.EmTmError, emtm.em_get_length, 0)
        self.assertRaises(emtm.EmTmError, emtm.em_get_length, 1)
        r = emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        length_count = emtm.em_get_length_count()
        length = emtm.em_get_length(0)

        em_length_values = []
        em_length_fields = [field[0] for field in length._fields_]

        self.assertRaises(emtm.EmTmError, emtm.em_get_length, -1)
        for ii in range(length_count.total):
            em_length_values = []
            l = emtm.em_get_length(ii)
            for fields in em_length_fields:
                em_length_values.append(l.__getattribute__(fields))
        self.assertRaises(emtm.EmTmError, emtm.em_get_length, ii + 1)

    def test_tm_load_data(self):
        self.assertRaises(emtm.EmTmError, emtm.tm_load_data, "fake path")
        self.assertRaises(emtm.EmTmError, emtm.tm_load_data, "/totally/fake/and/made/up/path/which/surely/doesnt/exist/on/anyones/machine")
        self.assertRaises(emtm.EmTmError, emtm.tm_load_data, "")
        emtm.tm_load_data(os.path.join(TEST_FILES_PATH, 'Test.TMObs'))

    def test_tm_clear_data(self):
        emtm.tm_load_data(os.path.join(TEST_FILES_PATH, 'Test.TMObs'))
        emtm.tm_clear_data()

    def test_tm_point_count(self):
        r = emtm.tm_load_data(os.path.join(TEST_FILES_PATH, 'Test.TMObs'))
        r = emtm.tm_point_count()
        self.assertEqual(r, 10)

    def test_tm_get_point(self):
        self.assertRaises(emtm.EmTmError, emtm.tm_get_point, -1)
        self.assertRaises(emtm.EmTmError, emtm.tm_get_point, 0)
        self.assertRaises(emtm.EmTmError, emtm.tm_get_point, 1)
        r = emtm.tm_load_data(os.path.join(TEST_FILES_PATH, 'Test.TMObs'))
        point_count = emtm.tm_point_count()
        p = emtm.tm_get_point(0)

        tm_point_values = []
        tm_point_fields = [field[0] for field in p._fields_]

        self.assertRaises(emtm.EmTmError, emtm.tm_get_point, -1)
        for ii in range(point_count):
            tm_point_values = []
            p = emtm.tm_get_point(ii)
            for fields in tm_point_fields:
                tm_point_values.append(p.__getattribute__(fields))
        self.assertRaises(emtm.EmTmError, emtm.tm_get_point, ii + 1)

    def test_em_to_dataframe(self):
        emtm.em_load_data(os.path.join(TEST_FILES_PATH, 'Test.EMObs'))
        length_dataframe = emtm.em_to_dataframe(em_data_type='length')
        point_dataframe = emtm.em_to_dataframe(em_data_type='point')

        points_df = emtm.EmAnnotationDataFrames.load_points_from_current_em_file()
        points3d_df = emtm.EmAnnotationDataFrames.load_3d_points_from_current_em_file()
        lengths_df = emtm.EmAnnotationDataFrames.load_lengths_from_current_em_file()
        self.assertEqual(len(points_df), 35)
        self.assertEqual(len(points3d_df), 2)
        self.assertEqual(len(lengths_df), 22)

        self.assertListEqual(list(points_df.columns), [field_info[0] for field_info in emtm.EmPointData._fields_])
        self.assertListEqual(list(points3d_df.columns), [field_info[0] for field_info in emtm.Em3DPpointData._fields_])
        self.assertListEqual(list(lengths_df.columns), [field_info[0] for field_info in emtm.EmLengthData._fields_])

    def test_starting_with_empty_EmAnnotationDataFrames_object(self):
        emtm.em_load_data(os.path.join(os.path.join(TEST_FILES_PATH, 'Test.EMObs')))
        dfs = emtm.EmAnnotationDataFrames(None, None, None)
        self.assertIs(dfs.points, None)
        self.assertIs(dfs.points3d, None)
        self.assertIs(dfs.lengths, None)
        dfs.points = emtm.EmAnnotationDataFrames.load_points_from_current_em_file()
        self.assertEqual(len(dfs.points), 35)

    def test_starting_with_partially_empty_EmAnnotationDataFrames_object(self):
        emtm.em_load_data(os.path.join(os.path.join(TEST_FILES_PATH, 'Test.EMObs')))
        dfs = emtm.EmAnnotationDataFrames(points=None)
        self.assertIs(dfs.points, None)
        self.assertEqual(len(dfs.points3d), 2)
        self.assertEqual(len(dfs.lengths), 22)

        dfs = emtm.EmAnnotationDataFrames(points=None)
        self.assertIs(dfs.points, None)
        self.assertEqual(len(dfs.points3d), 2)
        self.assertEqual(len(dfs.lengths), 22)

    def test_em_to_dataframes(self):
        emtm.em_load_data(os.path.join(os.path.join(TEST_FILES_PATH, 'Test.EMObs')))
        dfs = emtm.EmAnnotationDataFrames()
        self.assertEqual(len(dfs.points), 35)
        self.assertEqual(len(dfs.points3d), 2)
        self.assertEqual(len(dfs.lengths), 22)
