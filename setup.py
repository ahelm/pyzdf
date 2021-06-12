from Cython.Build import cythonize
from setuptools import Extension
from setuptools import setup

setup(
    ext_modules=cythonize(
        Extension(
            "pyzdf.zdf",
            ["pyzdf/zdf.pyx", "zpic/zdf/zdf.c"],
            include_dirs=["zpic/zdf"],
        ),
        compiler_directives={"language_level": 3},
    )
)
