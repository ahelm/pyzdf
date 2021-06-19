from contextlib import contextmanager
from enum import Enum
from pathlib import Path
from typing import Iterator
from typing import Literal
from typing import Union

ZDF_MAGIC_NUMBER: str

class zdf_data_type(Enum):
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

class zdf_file_access_mode(Enum):
    """ZDF file access modes"""

    create: Literal["create"]
    read: Literal["read"]
    update: Literal["update"]

def zdf_sizeof(data_type: zdf_data_type) -> int:
    """
    Returns size of a ZDF datatype

    Arguments:
        data_type: ID of the data type as `int` or `zdf_data_type`

    Raises:
        TypeError: If type of `data_type` is not of type `zdf_data_type`

    Returns:
        Type size in bytes or for an invalid data type
    """
    ...

class File:
    def __init__(self, path: Path, mode: zdf_file_access_mode) -> None:
        """
        Opens and potentially creates the ZDF file

        Arguments:
            path: Path to a ZDF file
            mode: Mode for ZDF file
        """
        ...
    @property
    def path(self) -> Path:
        """Path of the ZDF file"""
        ...
    @property
    def access_mode(self) -> zdf_file_access_mode:
        """Access mode of ZDF file"""
        ...
    def close(self):
        """Close opened ZDF file"""

@contextmanager
def open_zdf_file(
    filepath: Union[str, Path],
    mode: Union[Literal["create"], Literal["read"], Literal["update"]] = "create",
) -> Iterator[File]:
    """
    Opens a ZDF file and returns a `File` object

    Arguments:
        filepath:
            Path of ZDF file on disk
        mode:
            Mode for opening of ZDF file. Only `create`, `read`, and `update` supported
    """
    ...
