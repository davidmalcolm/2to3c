// Convert non-PyObject* deferences of "ob_type" to use Py_TYPE macro instead
@@
PyObject *py_obj_ptr;
type T; 
T non_py_obj_ptr;
@@
(
  py_obj_ptr->ob_type
|
- non_py_obj_ptr->ob_type
+ Py_TYPE(non_py_obj_ptr) 
)
