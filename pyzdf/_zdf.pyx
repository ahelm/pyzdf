cdef extern from "zdf.h":
    int ZDF_MAGIC_LENGTH
    int BYTES_PER_ZDF_UNIT

    const char* zdf_magic

ZDF_MAGIC_NUMBER = zdf_magic[:ZDF_MAGIC_LENGTH].decode()
