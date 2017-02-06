# 2to3c #
2to3c is a tool to help with porting Python 2 extensions written in C so that they will compile against both 2.6 and 3.1 (and possibly other versions of CPython)

It uses the [http://coccinelle.lip6.fr/ Coccinelle] tool to apply a series of "semantic patches" to .c files.

The aim of 2to3c is to simplify the porting process and reduce the amount of effort needed.  Unfortunately it's impossible to fully automate this process: typically you will need to decide whether your Python 2 "str" instances are bytes or encoded string data (Hopefully 2to3c makes the process much easier)

The project is in an early stage of development; it may or may not work, but has already saved time on at least one port to python 3 ([http://www.j5live.com/2010/02/03/the-quest-for-python-3/ dbus-python]).

# Fixes that 2to3c can make #
  - [https://fedorahosted.org/2to3c/browser/fixes/init-module.cocci Changes to module initialization API]
  - [https://fedorahosted.org/2to3c/browser/fixes/int-to-long.cocci Replacement of the PyInt with PyLong]
  - [https://fedorahosted.org/2to3c/browser/fixes/ob_type.cocci Changes to the location of the ob_type field within PyObject subclasses]
  - [https://fedorahosted.org/2to3c/browser/fixes/repr.cocci tp_repr methods should now return PyUnicode]
  - [https://fedorahosted.org/2to3c/browser/fixes/RO.cocci Eliminate usage of the #define alias RO for READONLY in structmember.h]
  - [https://fedorahosted.org/2to3c/browser/fixes/typeobject.py Use the PyVarObject_HEAD_INIT macro when initializing PyTypeObject instances] to cope with a change in the layout of these structures.
