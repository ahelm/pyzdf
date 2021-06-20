from enum import Enum
from pathlib import Path

import pytest

from pyzdf.zdf import ZDF_MAGIC_NUMBER
from pyzdf.zdf import File
from pyzdf.zdf import open_zdf_file
from pyzdf.zdf import zdf_data_type
from pyzdf.zdf import zdf_file_access_mode
from pyzdf.zdf import zdf_sizeof


def test_zdf_magic():
    """Check magic number of ZDF"""
    assert ZDF_MAGIC_NUMBER == "ZDF1"


def test_zdf_data_type_is_enum():
    """Check if 'zdf_data_type' is a valid Enum"""
    assert issubclass(zdf_data_type, Enum)


@pytest.mark.parametrize(
    "data_type",
    [
        zdf_data_type.null,
        zdf_data_type.int8,
        zdf_data_type.uint8,
        zdf_data_type.int16,
        zdf_data_type.uint16,
        zdf_data_type.int32,
        zdf_data_type.uint32,
        zdf_data_type.int64,
        zdf_data_type.uint64,
        zdf_data_type.float32,
        zdf_data_type.float64,
    ],
)
def test_all_types_zdf_data_type(data_type: zdf_data_type):
    """Check all supported ZDF datatypes"""
    assert isinstance(data_type, zdf_data_type)


def test_zdf_file_access_mode_is_enum():
    """Check if 'zdf_data_type' is a valid Enum"""
    assert issubclass(zdf_file_access_mode, Enum)


@pytest.mark.parametrize(
    "access_mode",
    [
        zdf_file_access_mode.create,
        zdf_file_access_mode.read,
        zdf_file_access_mode.update,
    ],
)
def test_zdf_file_access_mode_modes(access_mode: zdf_file_access_mode):
    """Check all file access modes"""
    assert isinstance(access_mode, zdf_file_access_mode)


@pytest.mark.parametrize(
    "mode_as_str, mode",
    [
        ("create", zdf_file_access_mode.create),
        ("read", zdf_file_access_mode.read),
        ("update", zdf_file_access_mode.update),
    ],
)
def test_zdf_file_access_mode_str_to_mode(mode_as_str: str, mode: zdf_file_access_mode):
    """Check conversion of string to mode"""
    assert zdf_file_access_mode.str_to_mode(mode_as_str) == mode


@pytest.mark.parametrize(
    "data_type, size",
    [
        (zdf_data_type.null, 0),
        (zdf_data_type.int8, 1),
        (zdf_data_type.uint8, 1),
        (zdf_data_type.int16, 2),
        (zdf_data_type.uint16, 2),
        (zdf_data_type.int32, 4),
        (zdf_data_type.uint32, 4),
        (zdf_data_type.float32, 4),
        (zdf_data_type.int64, 8),
        (zdf_data_type.uint64, 8),
        (zdf_data_type.float64, 8),
    ],
)
def test_zdf_sizeof(data_type: zdf_data_type, size: int):
    """Call 'zdf_sizeof' andcheck return value (should call C-Function)"""
    assert zdf_sizeof(data_type) == size


def test_zdf_sizeof_raises():
    """Raise TypeError when invalid type was passed"""
    with pytest.raises(TypeError, match="Invalid data type provided"):
        zdf_sizeof(-1)


def test_zdf_open_file(tmp_path: Path):
    """Open and create ZDF file and check if it was created"""
    new_file = tmp_path / "new.zdf"
    assert not new_file.exists()

    with open_zdf_file(new_file) as fp:
        assert isinstance(fp, File)
        assert fp.path == new_file
        assert fp.access_mode == zdf_file_access_mode.create

    assert new_file.exists()


def test_zdf_open_writes_magic_number(tmp_path: Path):
    """Check if magic number was written in ZDF file after creation"""
    new_file = tmp_path / "new.zdf"

    with open_zdf_file(new_file):
        pass

    with open(new_file, mode="r") as fp:
        assert fp.read() == ZDF_MAGIC_NUMBER
