from pyzdf.zdf import ZDF_MAGIC_NUMBER


def test_zdf_magic():
    assert ZDF_MAGIC_NUMBER == "ZDF1"
