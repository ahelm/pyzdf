from enum import Enum

from pyzdf.zdf import ZDF_MAGIC_NUMBER
from pyzdf.zdf import zdf_data_type
from pyzdf.zdf import zdf_file_access_mode


def test_zdf_magic():
    """Check magic number of ZDF"""
    assert ZDF_MAGIC_NUMBER == "ZDF1"


def test_zdf_data_type_is_enum():
    """Check if 'zdf_data_type' is a valid Enum"""
    assert issubclass(zdf_data_type, Enum)


def test_all_types_zdf_data_type():
    """Check all supported ZDF datatypes"""
    assert isinstance(zdf_data_type.null, zdf_data_type)
    assert isinstance(zdf_data_type.int8, zdf_data_type)
    assert isinstance(zdf_data_type.uint8, zdf_data_type)
    assert isinstance(zdf_data_type.int16, zdf_data_type)
    assert isinstance(zdf_data_type.uint16, zdf_data_type)
    assert isinstance(zdf_data_type.int32, zdf_data_type)
    assert isinstance(zdf_data_type.uint32, zdf_data_type)
    assert isinstance(zdf_data_type.int64, zdf_data_type)
    assert isinstance(zdf_data_type.uint64, zdf_data_type)
    assert isinstance(zdf_data_type.float32, zdf_data_type)
    assert isinstance(zdf_data_type.float64, zdf_data_type)


def test_zdf_file_access_mode_is_enum():
    """Check if 'zdf_data_type' is a valid Enum"""
    assert issubclass(zdf_file_access_mode, Enum)


def test_zdf_file_access_mode_modes():
    """Check all file access modes"""
    assert isinstance(zdf_file_access_mode.create, zdf_file_access_mode)
    assert isinstance(zdf_file_access_mode.read, zdf_file_access_mode)
    assert isinstance(zdf_file_access_mode.update, zdf_file_access_mode)
