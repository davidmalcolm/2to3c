@@
type T;
identifier FN;
identifier MOD_VAR;
expression MODULE_NAME, MODULE_METHODS, MODULE_DOC;
@@
+ #if PY_MAJOR_VERSION >= 3
+static struct PyModuleDef moduledef = {
+        PyModuleDef_HEAD_INIT,
+        MODULE_NAME,     /* m_name */
+        MODULE_DOC, /* m_doc */
+        0,           /* m_size */
+        MODULE_METHODS,        /* m_methods */
+        NULL,        /* m_reload */
+        NULL,        /* m_traverse */
+        NULL,        /* m_clear */
+        NULL,        /* m_free */
+};
+ #endif

T FN(void) {
   ...

+ #if PY_MAJOR_VERSION >= 3
+    MOD_VAR = PyModule_Create(&moduledef);
+ #else
     MOD_VAR = Py_InitModule3(MODULE_NAME, MODULE_METHODS, MODULE_DOC);
+ #endif

    ...
}
