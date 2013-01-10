#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''py2exe script to compile a single executable on Windows'''

from distutils.core import setup
import py2exe

includes = ["netifaces"]
dll_excludes = ["MSVCP90.dll", "libgdk-win32-2.0-0.dll",
"libgobject-2.0-0.dll", "tcl84.dll", "tk84.dll"]
excludes = ["_gtkagg", "_tkagg", "curses", "email", "pywin.debugger",
"pywin.debugger.dbgcon", "pywin.dialogs", "tcl",
"Tkconstants", "Tkinter"]
packages = []

setup(name='Interfaces',
        windows=['interfaces.pyw'],
        options = {
            "py2exe": {
                "compressed": 2,
                "optimize": 2,
                "packages": packages,
                "includes": includes,
                "excludes": excludes,
                "dll_excludes": dll_excludes,
                "bundle_files": 1,
                "dist_dir": 'dist',
                "xref": False,
                "skip_archive": False,
                "ascii": False,
                "custom_boot_script": ''
            },
        },
        zipfile = None
      )
