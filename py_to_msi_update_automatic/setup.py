#setup.py

# python setup.py bdist_msi
# pip install pypiwin32
# python -m pip install cx_freeze

from cx_Freeze import setup, Executable
setup(
    name = "script",
    version = "1.0.1",
    options = {"build_exe": {
        'packages': ["os","sys","ctypes","win32con"],
        'include_files': ['imagem.png'],
        'include_msvcr': True, # Colocar as DLLs do Microsoft Visual C++ Redistributable executável
    }},
    executables = [Executable("script.py",base="Win32GUI")]
    )


# AUTO UPDATE:
# * pip install esky