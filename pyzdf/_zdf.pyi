from enum import Enum
from typing import Literal

_zdf_magic: str

class _zdf_data_type(Enum):
    """
    ZDF datatypes

    Note:
        Only 'float32' and 'float64' are currently supported by ZDF.
    """

    null: Literal["null"]
    int8: Literal["int8"]
    uint8: Literal["uint8"]
    int16: Literal["int16"]
    uint16: Literal["uint16"]
    int32: Literal["int32"]
    uint32: Literal["uint32"]
    int64: Literal["int64"]
    uint64: Literal["uint64"]
    float32: Literal["float32"]
    float64: Literal["float64"]

class _zdf_file_access_mode(Enum):
    """ZDF file access modes"""

    create: Literal["create"]
    read: Literal["read"]
    update: Literal["update"]
