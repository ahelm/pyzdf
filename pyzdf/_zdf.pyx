from enum import Enum


cdef extern from "zdf.h":
    int ZDF_MAGIC_LENGTH
    const char* zdf_magic
    cdef enum zdf_data_type:
        zdf_null
        zdf_int8
        zdf_uint8
        zdf_int16
        zdf_uint16
        zdf_int32
        zdf_uint32
        zdf_int64
        zdf_uint64
        zdf_float32
        zdf_float64

_zdf_magic = zdf_magic[:ZDF_MAGIC_LENGTH].decode()

class _zdf_data_type(Enum):
    null = zdf_data_type.zdf_null
    int8 = zdf_data_type.zdf_int8
    uint8 = zdf_data_type.zdf_uint8
    int16 = zdf_data_type.zdf_int16
    uint16 = zdf_data_type.zdf_uint16
    int32 = zdf_data_type.zdf_int32
    uint32 = zdf_data_type.zdf_uint32
    int64 = zdf_data_type.zdf_int64
    uint64 = zdf_data_type.zdf_uint64
    float32 = zdf_data_type.zdf_float32
    float64 = zdf_data_type.zdf_float64
