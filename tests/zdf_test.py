from enum import Enum

from pyzdf.zdf import ZDF_MAGIC_NUMBER, zdf_data_type


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
