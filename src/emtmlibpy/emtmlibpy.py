"""
Abstraction library for libEMTLib.so from SeaGIS.
Requires a licence to use, this is just a python wrapping function
"""
import ctypes
from enum import IntEnum, auto

EMTM_MAX_CHARS = 1024


class Result(IntEnum):
    """
    libStereoLibLX returns result codes.  This enumerates the codes.
    """
    ok = 0
    failed = auto()
    invalid_licence = auto()
    invalid_index = auto()
    buffer_too_small = auto()


class EmPointData(ctypes.Structure):
    """
    Point structures used by libEMTLib.so from SeaGIS
    """
    _fields_ = {
        ('str_op_code', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_filename', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('n_frame', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('str_period', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('d_period_time_mins', ctypes.c_double),
        ('d_imx', ctypes.c_double),
        ('d_imy', ctypes.c_double),
        ('d_rectx', ctypes.c_double),
        ('d_recty', ctypes.c_double),
        ('str_family', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_genus', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_species', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_code', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_number', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_stage', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_activity', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_comment', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_att_9', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_att_10', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS))
    }

    def __int__(self, str_op_code,
                str_filename,
                n_frame,
                d_time_mins,
                str_period,
                d_period_time_mins,
                d_imx, d_imy,
                d_rectx, d_recty,
                str_family, str_genus, str_species,
                str_code,
                str_number,
                str_stage,
                str_activity,
                str_comment,
                str_att_9, str_att_10):
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
    _fields_ = {
        ('str_op_code', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_filename_left', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_filename_right', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('n_frame_left', ctypes.c_int),
        ('n_frame_right', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('str_period', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
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
        ('str_family', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_genus', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_species', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_code', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_number', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_stage', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_activity', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_comment', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_att_9', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_att_10', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS))
    }

    def __int__(self, str_op_code,
                str_filename_left, str_filename_right,
                n_frame_left, n_frame_right,
                d_time_mins,
                str_period,
                d_period_time_mins,
                d_imx_left, d_imy_left, d_imx_right, d_imy_right,
                dx, dy, dz,
                dsx, dsy, dsz,
                d_rms,
                d_range,
                d_direction,
                str_family, str_genus, str_species,
                str_code,
                str_number,
                str_stage,
                str_activity,
                str_comment,
                str_att_9, str_att_10):
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
    _fields_ = {
        ('str_op_code', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_filename_left', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_filename_right', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('n_frame_left', ctypes.c_int),
        ('n_frame_right', ctypes.c_int),
        ('d_time_mins', ctypes.c_double),
        ('str_period', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
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
        ('str_family', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_genus', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_species', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_code', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_number', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_stage', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_activity', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_comment', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_att_9', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS)),
        ('str_att_10', ctypes.create_string_buffer(b'', EMTM_MAX_CHARS))
    }

    def __int__(self, str_op_code,
                str_filename_left, str_filename_right,
                n_frame_left, n_frame_right,
                d_time_mins,
                str_period,
                d_period_time_mins,
                b_compound_length,
                d_imx1_left, d_imy1_left, d_imx1_right, d_imy1_right,
                d_imx2_left, d_imy2_left, d_imx2_right, d_imy2_right,
                d_length,
                d_precision,
                d_rms,
                d_range,
                d_direction,
                dx_mid, dy_mid, dz_mid,
                str_family, str_genus, str_species,
                str_code,
                str_number,
                str_stage,
                str_activity,
                str_comment,
                str_att_9, str_att_10):
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
