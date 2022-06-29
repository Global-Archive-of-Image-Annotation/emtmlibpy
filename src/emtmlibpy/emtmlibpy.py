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


