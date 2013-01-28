#Interfaces

GUI application to list informations about network interfaces

The application requires following modules:
- wxPython
- netifaces (http://alastairs-place.net/projects/netifaces/)

Just run the application with:
```python interfaces.pyw```

To generate an executable you also need py2exe
Command to compile the .exe:
```python setup.py py2exe```

Actuallly, the compiled executable won't run, instead it throws an ImportError and I have no clue how to resolve this issue, so if anyone knows how to fix this, feel free to contribute.
That's the error from the log file:

    Traceback (most recent call last):
    File "interfaces.pyw", line 5, in <module>
    File "zipextimporter.pyo", line 98, in load_module
    ImportError: MemoryLoadLibrary failed loading netifaces.pyd
