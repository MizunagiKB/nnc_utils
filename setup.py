# -*- coding: utf-8 -*-
# ------------------------------------------------------------------ import(s)
import sys
from cx_Freeze import setup, Executable


# ------------------------------------------------------------------- param(s)
VERSION = "1.0.0"


build_exe_options = {
    "packages": ["os"],
    "includes": ["numpy", "numpy.core._methods", "numpy.lib.format"],
    "excludes": [
        "acyncio", "certifi", "chardet", "cloudpickle",
        "colorama",
        "concurrent",
        "curses",
        "dateutil",
        "distutils",
        "email",
        "html",
        "http",
        "idna",
        "jinja2",
        "json", "jsonschema", "jupyter_client", "jupyter_core",
        "lib2to3", "markupsafe", "matplotlib",
        "notebook",
        "parso",
        "pydoc",
        "pydoc_data",
        "pywt",
        "tkinter",
        "unittest",
        "urllib",
        "xml",
        "xmlrpc"
    ],
    "include_files": ["chk_image_dup.bat"]
}

base_cui = None
base_gui = None
if sys.platform == "win32":
    base_gui = "Win32GUI"

setup(
    name="nnc_utils",
    version=VERSION,
    description="Image utils for Neural Network Console",
    options={"build_exe": build_exe_options},
    executables=[
        Executable("chk_image_dup.py", base=base_cui),
        Executable("gen_image_dataset.py", base=base_cui),
        Executable("nnc_utils.py", base=base_gui)
    ]
)



# [EOF]
