from enum import Enum

from ._zdf cimport zdf_data_type as _zdf_data_type
from ._zdf cimport zdf_file_access_mode as _zdf_file_access_mode
from ._zdf cimport zdf_magic
from ._zdf cimport zdf_sizeof as _zdf_sizeof

ZDF_MAGIC_NUMBER = zdf_magic.decode()

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
