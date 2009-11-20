// tp_repr functions should return unicode in py3k
// FIXME: need to restrict to just tp_repr functions:
@@
type T;
function FN_repr;
expression E;
@@
PyObject *
FN_repr(T *self)
{
     ...     
-    return PyString_FromString(E);
+    return PyUnicode_FromString(E);
}

@@
type T;
function FN_repr;
expression E1, E2;
@@
PyObject *
FN_repr(T *self)
{
     ...     
-    return PyString_FromFormat(E1, E2);
+    return PyUnicode_FromFormat(E1, E2);
}
