from libc.stddef cimport size_t
from libc.stdint cimport uint32_t
from libc.stdint cimport uint64_t
from libc.stdint cimport int32_t
from libc.stdio cimport FILE

cdef extern from "zdf.h":
    # Macros defined inside 'zdf.h'
    DEF BYTES_PER_ZDF_UNIT = 4
    DEF ZDF_MAGIC_LENGTH = BYTES_PER_ZDF_UNIT

    # Maximum array dimensions for zdf files
    DEF zdf_max_dims = 3

    # Magic byte sequence for identifying ZDF files
    const char zdf_magic[ZDF_MAGIC_LENGTH]

    # ZDF data types
    enum zdf_data_type:
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

    # ZDF file access modes
    enum zdf_file_access_mode:
        ZDF_CREATE
        ZDF_READ
        ZDF_UPDATE

    # ZDF file struct
    ctypedef struct t_zdf_file:
        FILE *fp
        zdf_file_access_mode mode
        uint32_t ndatasets

    # ZDF dataset struct
    ctypedef struct t_zdf_dataset:
        zdf_data_type data_type
        uint32_t ndims
        uint64_t count[zdf_max_dims]
        void *data
        uint64_t id
        uint64_t offset

    # ZDF chunks
    ctypedef struct t_zdf_chunk:
        uint64_t count[zdf_max_dims]
        uint64_t start[zdf_max_dims]
        uint64_t stride[zdf_max_dims]
        void * data

    # ZDF axis types
    enum zdf_axis_type:
        zdf_linear
        zdf_log10
        zdf_log2

    # ZDF grid axis
    ctypedef struct t_zdf_grid_axis:
        zdf_axis_type type
        double min_ "min"
        double max_ "max"
        char* label
        char* units

    # ZDF iteration
    ctypedef struct t_zdf_iteration:
        int32_t n
        double t
        char* time_units

    ctypedef struct t_zdf_grid_info:
        uint32_t ndims
        uint64_t count[zdf_max_dims]
        char* label
        char* units
        t_zdf_grid_axis *axis

    # ZDF particle info
    ctypedef struct t_zdf_part_info:
        char* name
        uint64_t np
        uint32_t nquants
        char** quants
        char** labels
        char** units

    # ZDF track info
    ctypedef struct t_zdf_track_info:
        char* name
        uint32_t ntracks
        uint32_t ndump
        uint32_t niter
        uint32_t nquants
        char** quants
        char** labels
        char** units

    # Low level interface
    size_t zdf_sizeof(zdf_data_type data_type)
    int zdf_open_file(t_zdf_file* zdf, const char* filename, zdf_file_access_mode mode)
    int zdf_close_file(t_zdf_file* zdf)
    size_t zdf_vector_write(
        t_zdf_file* zdf,
        const void* data,
        zdf_data_type data_type,
        size_t len
    )
    size_t zdf_add_string(
        t_zdf_file* zdf,
        const char* name,
        const char* str
    )
    size_t zdf_add_int32(t_zdf_file* zdf, const char* name, const int32_t value)
    size_t zdf_add_double(t_zdf_file* zdf, const char* name, const double value)
    size_t zdf_add_iteration(
        t_zdf_file* zdf,
        const char* name,
        const t_zdf_iteration* iter
    )
    size_t zdf_add_grid_info(
        t_zdf_file* zdf,
        const char* name,
        const t_zdf_grid_info* grid
    )
    size_t zdf_add_part_info(t_zdf_file* zdf, const char* name, t_zdf_part_info* part)
    size_t zdf_add_track_info(
        t_zdf_file* zdf,
        const char* name,
        t_zdf_track_info* tracks
    )
    size_t zdf_add_dataset(t_zdf_file* zdf, const char* name, t_zdf_dataset* dataset)

    # Chunked dataset interface
    size_t zdf_start_cdset(t_zdf_file* zdf, const char* name, t_zdf_dataset* dataset)
    size_t size_zdf_chunk_header(const t_zdf_dataset* dataset)
    size_t zdf_write_chunk_header(
        t_zdf_file* zdf,
        t_zdf_dataset* dataset,
        t_zdf_chunk* chunk
    )
    size_t zdf_write_cdset( t_zdf_file* zdf, t_zdf_dataset* dataset, t_zdf_chunk* chunk)
    size_t zdf_end_cdset(t_zdf_file* zdf, t_zdf_dataset* dataset)
    size_t zdf_open_dataset(t_zdf_file* zdf, const char* name, t_zdf_dataset* dataset)
    int zdf_extend_dataset(t_zdf_file* zdf, t_zdf_dataset* dataset, uint64_t* new_count)
