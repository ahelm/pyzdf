from Cython.Build import cythonize
from setuptools import Extension, setup

setup(
    ext_modules=cythonize(
        Extension(
            "pyzdf._zdf",
            ["pyzdf/_zdf.pyx", "zpic/zdf/zdf.c"],
            include_dirs=["zpic/zdf"],
        ),
        compiler_directives={"language_level": 3},
    )
)
