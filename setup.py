import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "excludes": ["_gtkagg", "_tkagg", "bsddb", "curses", "email", "pywin.debugger", "pywin.debugger.dbgcon",
                 "pywin.dialogs", "tcl", "Tkconstants", "Tkinter"],
    "optimize": 2,
    "compressed": True
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "pywintar",
      version = "0.1",
      description = "Python Windows Tarfile Application",
      options = {"build_exe": build_exe_options},
      executables = [Executable("pywintar.py", base=base)])