"""
Abstraction library for libEMTLib.so from SeaGIS.
Requires a licence to use, this is just a python wrapping function
"""
import ctypes
import dataclasses
import typing
from enum import IntEnum, auto
from collections import namedtuple
import pandas as pd
import numpy as np

EMTM_MAX_CHARS = 1024
libc = ctypes.CDLL('libEMTMLib.so')


class EmTmError(Exception):
    def __int__(self, error: "EMTMResult", *args, **kwargs):
        super(EmTmError, self).__int__(f"EMTMLib returned error code {error.value} ({error.name}).")


class EMTMResult(IntEnum):
    """
    libStereoLibLX returns result codes.  This enumerates the codes.
    """
    ok = 0
    failed = auto()
    invalid_licence = auto()
    invalid_index = auto()
    buffer_too_small = auto()

    def check(self):
        if self.value != self.ok:
            raise EmTmError(self)


class EmPointData(ctypes.Structure):
    """
    Point structures used by libEMTLib.so from SeaGIS
    """
    _fields_ = [
        ('str_op_code', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_filename', ctypes.c_char * EMTM_MAX_CHARS),
        ('n_frame', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('str_period', ctypes.c_char * EMTM_MAX_CHARS),
        ('d_period_time_mins', ctypes.c_double),
        ('d_imx', ctypes.c_double),
        ('d_imy', ctypes.c_double),
        ('d_rectx', ctypes.c_double),
        ('d_recty', ctypes.c_double),
        ('str_family', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_genus', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_species', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_code', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_number', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_stage', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_activity', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_comment', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_9', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_10', ctypes.c_char * EMTM_MAX_CHARS)
    ]

    def __init__(self, str_op_code=b'',
                str_filename=b'',
                n_frame=0,
                d_time_mins=0.0,
                str_period=b'',
                d_period_time_mins=0.0,
                d_imx=0.0, d_imy=0.0,
                d_rectx=0.0, d_recty=0.0,
                str_family=b'', str_genus=b'', str_species=b'',
                str_code=b'',
                str_number=b'',
                str_stage=b'',
                str_activity=b'',
                str_comment=b'',
                str_att_9=b'', str_att_10=b''):
        super().__init__()
        self.str_op_code = str_op_code
        self.str_filename = str_filename
        self.n_frame = n_frame
        self.d_time_mins = d_time_mins
        self.str_period = str_period
        self.d_period_time_mins = d_period_time_mins
        self.d_imx = d_imx
        self.d_imy = d_imy
        self.d_rectx = d_rectx
        self.d_recty = d_recty
        self.str_family = str_family
        self.str_genus = str_genus
        self.str_species = str_species
        self.str_code = str_code
        self.str_number = str_number
        self.str_stage = str_stage
        self.str_activity = str_activity
        self.str_comment = str_comment
        self.str_att_9 = str_att_9
        self.str_att_10 = str_att_10


class Em3DPpointData(ctypes.Structure):
    """
    3DPoint structures used by libEMTLib.so from SeaGIS
    """
    _fields_ = [
        ('str_op_code', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_filename_left', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_filename_right', ctypes.c_char * EMTM_MAX_CHARS),
        ('n_frame_left', ctypes.c_int),
        ('n_frame_right', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('str_period', ctypes.c_char * EMTM_MAX_CHARS),
        ('d_period_time_mins', ctypes.c_double),
        ('d_imx_left', ctypes.c_double),
        ('d_imy_left', ctypes.c_double),
        ('d_imx_right', ctypes.c_double),
        ('d_imy_right', ctypes.c_double),
        ('dx', ctypes.c_double),
        ('dy', ctypes.c_double),
        ('dz', ctypes.c_double),
        ('dsx', ctypes.c_double),
        ('dsy', ctypes.c_double),
        ('dsz', ctypes.c_double),
        ('d_rms', ctypes.c_double),
        ('d_range', ctypes.c_double),
        ('d_direction', ctypes.c_double),
        ('str_family', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_genus', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_species', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_code', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_number', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_stage', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_activity', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_comment', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_9', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_10', ctypes.c_char * EMTM_MAX_CHARS)
    ]

    def __init__(self, str_op_code=b'',
                str_filename_left=b'', str_filename_right=b'',
                n_frame_left=0, n_frame_right=0,
                d_time_mins=0.0,
                str_period=b'',
                d_period_time_mins=0.0,
                d_imx_left=0.0, d_imy_left=0.0, d_imx_right=0.0, d_imy_right=0.0,
                dx=0.0, dy=0.0, dz=0.0,
                dsx=0.0, dsy=0.0, dsz=0.0,
                d_rms=0.0,
                d_range=0.0,
                d_direction=0.0,
                str_family=b'', str_genus=b'', str_species=b'',
                str_code=b'',
                str_number=b'',
                str_stage=b'',
                str_activity=b'',
                str_comment=b'',
                str_att_9=b'', str_att_10=b''):
        super().__init__()
        self.str_op_code = str_op_code
        self.str_filename_left = str_filename_left
        self.str_filename_right = str_filename_right
        self.n_frame_left = n_frame_left
        self.n_frame_right = n_frame_right
        self.d_time_mins = d_time_mins
        self.str_period = str_period
        self.d_period_time_mins = d_period_time_mins
        self.d_imx_left = d_imx_left
        self.d_imy_left = d_imy_left
        self.d_imx_right = d_imx_right
        self.d_imy_right = d_imy_right
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.dsx = dsx
        self.dsy = dsy
        self.dsz = dsz
        self.d_rms = d_rms
        self.d_range = d_range
        self.d_direction = d_direction
        self.str_family = str_family
        self.str_genus = str_genus
        self.str_species = str_species
        self.str_code = str_code
        self.str_number = str_number
        self.str_stage = str_stage
        self.str_activity = str_activity
        self.str_comment = str_comment
        self.str_att_9 = str_att_9
        self.str_att_10 = str_att_10


class EmLengthData(ctypes.Structure):
    """
    Length structures used by libEMTLib.so from SeaGIS
    """
    _fields_ = [
        ('str_op_code', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_filename_left', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_filename_right', ctypes.c_char * EMTM_MAX_CHARS),
        ('n_frame_left', ctypes.c_int),
        ('n_frame_right', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('str_period', ctypes.c_char * EMTM_MAX_CHARS),
        ('d_period_time_mins', ctypes.c_double),
        ('b_compound_length', ctypes.c_bool),
        ('d_imx1_left', ctypes.c_double),
        ('d_imy1_left', ctypes.c_double),
        ('d_imx1_right', ctypes.c_double),
        ('d_imy1_right', ctypes.c_double),
        ('d_imx2_left', ctypes.c_double),
        ('d_imy2_left', ctypes.c_double),
        ('d_imx2_right', ctypes.c_double),
        ('d_imy2_right', ctypes.c_double),
        ('d_length', ctypes.c_double),
        ('d_precision', ctypes.c_double),
        ('d_rms', ctypes.c_double),
        ('d_range', ctypes.c_double),
        ('d_direction', ctypes.c_double),
        ('dx_mid', ctypes.c_double),
        ('dy_mid', ctypes.c_double),
        ('dz_mid', ctypes.c_double),
        ('str_family', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_genus', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_species', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_code', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_number', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_stage', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_activity', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_comment', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_9', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_10', ctypes.c_char * EMTM_MAX_CHARS)
    ]

    def __init__(self, str_op_code=b'',
                str_filename_left=b'', str_filename_right=b'',
                n_frame_left=0, n_frame_right=0,
                d_time_mins=0.0,
                str_period=b'',
                d_period_time_mins=0.0,
                b_compound_length=0.0,
                d_imx1_left=0.0, d_imy1_left=0.0, d_imx1_right=0.0, d_imy1_right=0.0,
                d_imx2_left=0.0, d_imy2_left=0.0, d_imx2_right=0.0, d_imy2_right=0.0,
                d_length=0.0,
                d_precision=0.0,
                d_rms=0.0,
                d_range=0.0,
                d_direction=0.0,
                dx_mid=0.0, dy_mid=0.0, dz_mid=0.0,
                str_family=b'', str_genus=b'', str_species=b'',
                str_code=b'',
                str_number=b'',
                str_stage=b'',
                str_activity=b'',
                str_comment=b'',
                str_att_9=b'', str_att_10=b''):
        super().__init__()
        self.str_op_code = str_op_code
        self.str_filename_left = str_filename_left
        self.str_filename_right = str_filename_right
        self.n_frame_left = n_frame_left
        self.n_frame_right = n_frame_right
        self.d_time_mins = d_time_mins
        self.str_period = str_period
        self.d_period_time_mins = d_period_time_mins
        self.b_compound_length = b_compound_length
        self.d_imx1_left = d_imx1_left
        self.d_imy1_left = d_imy1_left
        self.d_imx1_right = d_imx1_right
        self.d_imy1_right = d_imy1_right
        self.d_imx2_left = d_imx2_left
        self.d_imy2_left = d_imy2_left
        self.d_imx2_right = d_imx2_right
        self.d_imy2_right = d_imy2_right
        self.d_length = d_length
        self.d_precision = d_precision
        self.d_rms = d_rms
        self.d_range = d_range
        self.d_direction = d_direction
        self.dx_mid = dx_mid
        self.dy_mid = dy_mid
        self.dz_mid = dz_mid
        self.str_family = str_family
        self.str_genus = str_genus
        self.str_species = str_species
        self.str_code = str_code
        self.str_number = str_number
        self.str_stage = str_stage
        self.str_activity = str_activity
        self.str_comment = str_comment
        self.str_att_9 = str_att_9
        self.str_att_10 = str_att_10


class TmPointData(ctypes.Structure):
    """
    Point structures used by libEMTLib.so from SeaGIS
    """
    _fields_ = [
        ('str_filename', ctypes.c_char * EMTM_MAX_CHARS),
        ('n_frame', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('d_image_row', ctypes.c_double),
        ('d_image_col', ctypes.c_double),
        ('str_att_1', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_2', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_3', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_4', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_5', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_6', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_7', ctypes.c_char * EMTM_MAX_CHARS),
        ('str_att_8', ctypes.c_char * EMTM_MAX_CHARS)
    ]

    def __init__(self,
                str_filename=b'',
                n_frame=0,
                d_time_mins=0.0,
                d_image_row=0.0,
                d_image_col=0.0,
                str_att_1=b'', str_att_2=b'', str_att_3=b'', str_att_4=b'', str_att_5=b'', str_att_6=b'', str_att_7=b'',
                str_att_8=b''):
        super().__init__()
        self.str_filename = str_filename
        self.n_frame = n_frame
        self.d_time_mins = d_time_mins
        self.d_image_row = d_image_row
        self.d_image_col = d_image_col
        self.str_att_1 = str_att_1
        self.str_att_2 = str_att_2
        self.str_att_3 = str_att_3
        self.str_att_4 = str_att_4
        self.str_att_5 = str_att_5
        self.str_att_6 = str_att_6
        self.str_att_7 = str_att_7
        self.str_att_8 = str_att_8


def emtm_version() -> tuple[int, int]:
    """
    Return the version number of libStereoLibLX
    :return: (major, minor)
    """

    minor = ctypes.c_int(0)
    major = ctypes.c_int(0)

    libc.EMTMVersion(ctypes.byref(major), ctypes.byref(minor))

    return major.value, minor.value


def emtm_licence_present() -> bool:
    """
    Checks to see if there is a valid licence present
    :return:
    """
    r = libc.EMTMLicencePresent()

    return True if r == 1 else False


def em_load_data(filename: str) -> None:
    """
    The EventMeasure data file (.EMObs) to load

    Use this function to load an EventMeasure data file.
    The EventMeasure data loaded with this function remains persistent
    within the library until a subsequent call to this function is made, or the
    data is specifically cleared by calling `EMClearData`.

    Essentially all remaining functions that deal with EventMeasure data rely
    on this function to load the actual data.

    You do not need to call `EMClearData` before calling this function.

    :param filename:
    :raises EmTmError if the underlying library does not return "OK"
    :return: None
    """
    EMTMResult(libc.EMLoadData(bytes(filename, 'UTF-8'))).check()


def em_clear_data() -> None:
    """
    Use this function to clear data loaded with EMLoadData. The only reason to
    use this function is to specifically release resources used to store the
    current EventMeasure data. Those resources are automatically released
    when the library goes out of scope, or EMLoadData is used to load other
    EventMeasure data.

    :return: None
    """
    libc.EMClearData()


def em_op_code(n_buff_sz: int = EMTM_MAX_CHARS) -> str:
    """
    Use this function to get the OpCode of the currently loaded EventMeasure
    data. The EventMeasure data is loaded using EMLoadData.

    :param p_str_op_code: Address of the buffer to receive the OpCode string. The caller is
    responsible for allocating enough space for at least nBuffSz
    characters in this buffer.
    :param n_buff_sz: The size of the buffer (pStrOpCode)
    :raises EmTmError if the underlying library does not return "OK"
    :return: Will return buffer_too_small if the OpCode will not fit in the
    supplied buffer, ok for success.
    """

    op_code = ctypes.create_string_buffer(n_buff_sz)

    EMTMResult(libc.EMOpCode(ctypes.byref(op_code), n_buff_sz)).check()

    return op_code.value.decode()


def em_units(n_buff_sz: int = EMTM_MAX_CHARS) -> str:
    """
    Use this function to get the 3D measurement units for the currently loaded
    EventMeasure data. The EventMeasure data is loaded using EMLoadData

    :param p_str_units: Address of the buffer to receive the units string. The caller is
    responsible for allocating enough space for at least nBuffSz
    characters in this buffer.
    :param n_buff_sz: The size of the buffer (pStrUnits).
    :raises EmTmError if the underlying library does not return "OK"
    :return: Will return buffer_too_small if the units string will not fit in the
    supplied buffer, ok for success.
    """

    p_str_units = ctypes.create_string_buffer(n_buff_sz)

    EMTMResult(libc.EMUnits(ctypes.byref(p_str_units))).check()

    return p_str_units.value.decode()


def em_unique_fgs() -> int:
    """
    Use this function to find the number of unique family, genus, species
    combinations present in all measurements in the currently loaded
    EventMeasure data. All measurement types are considered (points,
    bounding boxes, 3D points and lengths).

    EventMeasure data is loaded using EMLoadData.
    This function must be called before calling EMGetUniqueFGS for two
    reasons:

    • Calling EMUniqueFGS generates a list of unique family, genus, species
    values for the currently loaded EventMeasure data. The library stores
    this list until a new EventMeasure data file is loaded (EMLoadData) or
    the current EventMeasure data is specifically cleared (EMClearData).

    • EMUniqueFGS returns the number of family, genus, species names
    that can be queried using EMGetUniqueFGS.

    It is sufficient to call this function (EMUniqueFGS) once before making
    multiple calls to EMGetUniqueFGS.

    :return:
    """
    return libc.EMUniqueFGS()


def em_get_unique_fgs(n_index: int) -> tuple:
    """
    Before using this function:

    • There must be EventMeasure data loaded using EMLoadData.

    • You must call EMUniqueFGS to discover the number of unique family,
    genus, species combinations – this provides the upper bound for this
    function’s nIndex parameter.

    The returned family, genus, species strings will always be lower case,
    regardless of how they were originally stored in the EventMeasure data.
    It is possible (valid) for this function to return empty strings (“”) for the
    family, genus, species. An EventMeasure user may only annotate to the
    family level (so the genus and species are empty), or a user may not
    annotate the family, genus, species at all (for example an annotation or
    measurement that just has a comment attribute).

    The caller is responsible for allocating and deleting the buffers associated
    with the strings pStrFamily, pStrGenus, pStrSpecies; and ensuring the
    buffers are at least nBuffSz characters in size.

    Family, genus, species has some sample test data.
    :return: 
    :raises EmTmError if the underlying library does not return "OK"
    """

    n_index = ctypes.c_int(n_index)

    p_str_family = ctypes.create_string_buffer(EMTM_MAX_CHARS)
    p_str_genus = ctypes.create_string_buffer(EMTM_MAX_CHARS)
    p_str_species = ctypes.create_string_buffer(EMTM_MAX_CHARS)

    success = libc.EMGetUniqueFGS(n_index,
                                  ctypes.byref(p_str_family), ctypes.byref(p_str_genus), ctypes.byref(p_str_species),
                                  EMTM_MAX_CHARS)
    EMTMResult(success).check()

    return p_str_family.value.decode(), p_str_genus.value.decode(), p_str_species.value.decode()


def em_measurement_count_fgs(family: str, genus: str, species: str) -> tuple:
    """
    Use this function to query the number of measurements present in the
    currently loaded EventMeasure data, for a specified family/genus/species.
    The EventMeasure data is loaded using EMLoadData.

    The pStrFamily, pStrGenus, pStrSpecies arguments are used to
    query the measurement count for a specific family/genus/species.

    Specification of the family/genus/species is case insensitive.

    A wildcard “*” can be used to ignore a family/genus/species argument. For
    example, to count measurements for species ghi for any family and genus

    the first three arguments of the function call are:
    EMMeasurementCountFGS(“*”, “*”, “ghi”, ...);

    The family/genus/species arguments are case insensitive, so the following

    gives an identical result:
    EMMeasurementCountFGS(“*”, “*”, “GHI”, ...);

    To count measurements for family abc, genus def, species ghi the first

    three arguments of the function call are:
    EMMeasurementCountFGS(“abc”, “def”, “ghi”, ...);

    :param family: The family to use when counting measurements, see examples
    below.
    :param genus: The genus to use when counting measurements.
    :param species: The species to use when counting measurements.
    :return: (n_point, n_box, n_3D_point, n_length, n_cpd_length)
    """

    n_point = ctypes.c_int(0)
    n_box = ctypes.c_int(0)
    n_3D_point = ctypes.c_int(0)
    n_length = ctypes.c_int(0)
    n_cpd_length = ctypes.c_int(0)

    libc.EMMeasurementCountFGS(bytes(family, 'UTF-8'),
                               bytes(genus, 'UTF-8'),
                               bytes(species, 'UTF-8'),
                               ctypes.byref(n_point),
                               ctypes.byref(n_box),
                               ctypes.byref(n_3D_point),
                               ctypes.byref(n_length),
                               ctypes.byref(n_cpd_length))

    FGS = namedtuple('FGS', 'point box xyz_point, length cpd_length')
    fgs = FGS(n_point.value, n_box.value, n_3D_point.value, n_length.value, n_cpd_length.value)

    return fgs


def em_point_count() -> tuple:
    """
    Use this function to find the number of point measurements (including
    bounding boxes) in the currently loaded EventMeasure data.
    EventMeasure data is loaded using EMLoadData.

    This function must be called before calling EMGetPoint for two reasons:

    • Calling this function generates an indexed mapping of all point
    measurements in the currently loaded EventMeasure data. The
    library stores this mapping internally until a new EventMeasure data
    file is loaded (EMLoadData) or the current EventMeasure data is
    specifically cleared (EMClearData).

    • The return value of this function is the upper bound of the indices
    allowed by EMGetPoint.

    It is sufficient to call this function once before making multiple calls to
    EMGetPoint.
    :return:
    """

    pn_bbox = ctypes.c_int(0)
    r = libc.EMPointCount(ctypes.byref(pn_bbox))

    PointCount = namedtuple('PointCount', 'total bbox')
    point_count = PointCount(r, pn_bbox.value)

    return point_count


def em_get_point(n_index: int) -> EmPointData:
    """
    Use this function to get point measurement data (including bounding box
    data) for a measurement in the currently loaded EventMeasure data.
    Before using this function:

    • There must be EventMeasure data loaded using EMLoadData.
    • You must call EMPointCount to discover the upper bound for this
    function’s nIndex parameter.

    If the function returns buffer_too_small, the string buffers in the
    EMPointData structure will be filled to their allowed capacity, then the
    string data is truncated to avoid overflow
    :param n_index:
    :raises EmTmError if the underlying library does not return "OK"
    :return:
    """

    p = EmPointData()

    r = libc.EMGetPoint(n_index, ctypes.byref(p))
    EMTMResult(r).check()

    return p


def em_3d_point_count() -> int:
    """
    Use this function to find the number of 3D point measurements in the
    currently loaded EventMeasure data.
    EventMeasure data is loaded using EMLoadData.

    This function must be called before calling EMGet3DPoint for two reasons:

    • Calling this function generates an indexed mapping of all 3D point
    measurements in the currently loaded EventMeasure data. The
    library stores this mapping internally until a new EventMeasure data
    file is loaded (EMLoadData) or the current EventMeasure data is
    specifically cleared (EMClearData).

    • The return value of this function is the upper bound of the indices
    allowed by EMGet3DPoint.

    It is sufficient to call this function once before making multiple calls to
    EMGet3DPoint

    :return: number of 3D points
    """

    r = libc.EM3DPointCount()
    return r


def em_get_3d_point(n_index: int) -> Em3DPpointData:
    """
    Use this function to get 3D point measurement data for a measurement in
    the currently loaded EventMeasure data.

    Before using this function:
    • There must be EventMeasure data loaded using EMLoadData.
    • You must call EM3DPointCount to discover the upper bound for this
    function’s nIndex parameter.

    If the function returns buffer_too_small, the string buffers in the
    EM3DPointData structure will be filled to their allowed capacity, then the
    string data is truncated to avoid overflow.
    :param n_index:
    :raises EmTmError if the underlying library does not return "OK"
    :return:
    """

    xyz_point = Em3DPpointData()

    r = libc.EMGet3DPoint(n_index, ctypes.byref(xyz_point))
    EMTMResult(r).check()

    return xyz_point


def em_get_length_count() -> tuple:
    """
    Use this function to find the number of length measurements (including
    compound lengths) in the currently loaded EventMeasure data.
    EventMeasure data is loaded using EMLoadData.

    This function must be called before calling EMGetLength for two reasons:
    • Calling this function generates an indexed mapping of all length
    measurements in the currently loaded EventMeasure data. The
    library stores this mapping internally until a new EventMeasure data
    file is loaded (EMLoadData) or the current EventMeasure data is
    specifically cleared (EMClearData).

    • The return value of this function is the upper bound of the indices
    allowed by EMGetLength.

    It is sufficient to call this function once before making multiple calls to
    EMGetLength.
    :return: The count of length measurements. This includes any compound
    length measurements (that is, the return value is the total number of
    length and compound length measurements). Use pnCompound to
    find the number of compound lengths
    """

    pn_compound = ctypes.c_int(0)

    r = libc.EMLengthCount(pn_compound)

    LengthCount = namedtuple('LengthCount', 'total compound')
    length_count = LengthCount(r, pn_compound.value)

    return length_count


def em_get_length(n_index: int) -> EmLengthData:
    """
    Use this function to get length measurement data (including compound
    length data) for a measurement in the currently loaded EventMeasure
    data.
    Before using this function:
    • There must be EventMeasure data loaded using EMLoadData.
    • You must call EMLengthCount to discover the upper bound for this
    function’s nIndex parameter.
    If the function returns buffer_too_small, the string buffers in the
    EMLengthData structure will be filled to their allowed capacity, then the
    string data is truncated to avoid overflow.

    :param n_index: The 0-based index of the required measurement. This value must be
    ≥ 0, and < the value returned by EMLengthCount.
    :raises EmTmError if the underlying library does not return "OK"
    :return:
    """

    length_data = EmLengthData()

    r = libc.EMGetLength(n_index, ctypes.byref(length_data))
    EMTMResult(r).check()

    return length_data


def tm_load_data(filename: str) -> None:
    """
    Use this function to load a TransectMeasure data file.
    The TransectMeasure data loaded with this function remains persistent
    within the library until a subsequent call to this function is made, or the
    data is specifically cleared by calling TMClearData.

    Essentially all remaining functions that deal with TransectMeasure data
    rely on this function to load the actual data.

    You do not need to call TMClearData before calling this function.

    :param filename: The TransectMeasure data file (.TMObs) to load.
    :raises: EmTmError if the underlying library does not return "OK"
    :return:
    """

    r = libc.TMLoadData(bytes(filename, 'UTF-8'))
    EMTMResult(r).check()


def tm_clear_data() -> None:
    """
    Use this function to clear data loaded with TMLoadData . The only reason to
    use this function is to specifically release resources used to store the
    current TransectMeasure data. Those resources are automatically released
    when the library goes out of scope, or TMLoadData is used to load other
    TransectMeasure data.

    :return:
    """

    libc.TMClearData()


def tm_point_count() -> int:
    """
    Use this function to find the number of point measurements in the
    currently loaded TransectMeasure data.
    TransectMeasure data is loaded using TMLoadData.
    This function must be called before calling TMGetPoint for two reasons:

    • Calling this function generates an indexed mapping of all point
    measurements in the currently loaded TransectMeasure data. The
    library stores this mapping internally until a new TransectMeasure
    data file is loaded (TMLoadData) or the current TransectMeasure
    data is specifically cleared (TMClearData).

    • The return value of this function is the upper bound of the indices
    allowed by TMGetPoint.

    It is sufficient to call this function once before making multiple calls to
    TMGetPoint.

    :return: The count of point measurements.
    """

    return libc.TMPointCount()


def tm_get_point(n_index) -> TmPointData:
    """
    Use this function to get point measurement data for a measurement in the
    currently loaded TransectMeasure data.
    Before using this function:
    • There must be TransectMeasure data loaded using TMLoadData.
    • You must call TMPointCount to discover the upper bound for this
    function’s nIndex parameter.
    If the function returns buffer_too_small , the string buffers in the
    TMPointData structure will be filled to their allowed capacity, then the
    string data is truncated to avoid overflow.


    :param n_index:
    :raises EmTmError if the underlying library does not return "OK"
    :return:
    """
    p = TmPointData()

    r = libc.TMGetPoint(n_index, ctypes.byref(p))
    EMTMResult(r).check()

    return p


def _dataframe_from_count_and_record_reader(count: int, record_read_function: typing.Callable[[int], ctypes.Structure]) -> pd.DataFrame:
    """
    A generic helper for generating a Pandas DataFrame from a given count and
    callable, returning a ctypes.Strucutre, representing a data record, given
    the index of the record (e.g. `em_get_length`).

    :param count: The number of records to read. Must be > 0 to get a valid DataFrame.
    :param record_read_function: Function returning records as ctypes.Structure, given an index.
    :return: The Pandas DataFrame
    """

    if count == 0:
        return None
    if count < 0:
        raise ValueError(f"Count must be greater than zero. Got {count}.")

    dtype_template = 'object'
    p = record_read_function(0)

    index = [attr for attr in dir(p) if (not attr.startswith('__') and not attr.startswith('_'))]
    data = np.empty(shape=[count, len(index)], dtype=dtype_template)  # change these

    for jj in range(count):
        p = record_read_function(jj)
        for ii, ind in enumerate(index):
            tmp = p.__getattribute__(ind)
            data[jj][ii] = tmp

    xpdf = pd.DataFrame(data=data, columns=index)
    xpdf = xpdf.convert_dtypes().infer_objects()
    return xpdf


def em_to_dataframe(em_data_type='length') -> pd.DataFrame:
    """
    A convenience method for returning a data frame instead of ctypes object.

    :param em_data_type: Either length or point
    :raises EmTmError if the underlying library does not return "OK"
    :return: pandas dataframe
    """
    if 'length' in em_data_type:
        count = em_get_length_count().total
        record_read_function = em_get_length
    elif 'point' in em_data_type:
        count = em_point_count().total
        record_read_function = em_get_point
    elif 'point3d' in em_data_type:
        count = em_3d_point_count()
        record_read_function = em_get_3d_point
    else:
        raise RuntimeError(f"Unsupported em_data_type `{em_data_type}`.")

    return _dataframe_from_count_and_record_reader(count, record_read_function)


@dataclasses.dataclass
class EmAnnotationDataFrames:
    """
    Helper class to represent the Pandas DataFrames which can be read from the an EMObs file and associate them with
    the relevant loading logic.

    By default, all three possible tables are read automatically, when instantiating this class. To avoid this
    behaviour for any of the tables, pass an explicit None for that table to the constructor.

    The contained static methods can be used to load only specific tables.
    """
    @staticmethod
    def load_points_from_current_em_file():
        return _dataframe_from_count_and_record_reader(em_point_count().total, em_get_point)

    @staticmethod
    def load_3d_points_from_current_em_file():
        return _dataframe_from_count_and_record_reader(em_3d_point_count(), em_get_3d_point)

    @staticmethod
    def load_lengths_from_current_em_file():
        return _dataframe_from_count_and_record_reader(em_get_length_count().total, em_get_length)

    points: pd.DataFrame = dataclasses.field(default_factory=load_points_from_current_em_file.__get__(object))
    points3d: pd.DataFrame = dataclasses.field(default_factory=load_3d_points_from_current_em_file.__get__(object))
    lengths: pd.DataFrame = dataclasses.field(default_factory=load_lengths_from_current_em_file.__get__(object))
