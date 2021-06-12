from enum import Enum

cdef extern from "zdf.h":
    int ZDF_MAGIC_LENGTH
    const char* zdf_magic
    enum _zdf_data_type "zdf_data_type":
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
    enum _zdf_file_access_mode "zdf_file_access_mode":
        ZDF_CREATE
        ZDF_READ
        ZDF_UPDATE
    size_t _zdf_sizeof "zdf_sizeof" (_zdf_data_type data_type)

ZDF_MAGIC_NUMBER = zdf_magic[:ZDF_MAGIC_LENGTH].decode()

class zdf_data_type(Enum):
    null = _zdf_data_type.zdf_null
    int8 = _zdf_data_type.zdf_int8
    uint8 = _zdf_data_type.zdf_uint8
    int16 = _zdf_data_type.zdf_int16
    uint16 = _zdf_data_type.zdf_uint16
    int32 = _zdf_data_type.zdf_int32
    uint32 = _zdf_data_type.zdf_uint32
    int64 = _zdf_data_type.zdf_int64
    uint64 = _zdf_data_type.zdf_uint64
    float32 = _zdf_data_type.zdf_float32
    float64 = _zdf_data_type.zdf_float64

class zdf_file_access_mode(Enum):
    create = _zdf_file_access_mode.ZDF_CREATE
    read = _zdf_file_access_mode.ZDF_READ
    update = _zdf_file_access_mode.ZDF_UPDATE

def zdf_sizeof(data_type):
    if isinstance(data_type, zdf_data_type):
        return _zdf_sizeof(data_type.value)
    else:
        raise TypeError("Invalid data type provided")
