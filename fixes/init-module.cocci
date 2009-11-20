@ mod_init_fn @
type T;
identifier FN;
identifier MOD_VAR;
expression MODULE_NAME, MODULE_METHODS, MODULE_DOC;
@@
T FN(void) {
   ...
   MOD_VAR = Py_InitModule3(MODULE_NAME, MODULE_METHODS, MODULE_DOC);
   ...
}

@@
type mod_init_fn.T;
identifier  mod_init_fn.FN;
identifier  mod_init_fn.MOD_VAR;
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
+#define MOD_ERROR_VAL NULL
+#else
+#endif

T FN(void) {
   ...

+ #if PY_MAJOR_VERSION >= 3
+    MOD_VAR = PyModule_Create(&moduledef);
+ #else
     MOD_VAR = Py_InitModule3(MODULE_NAME, MODULE_METHODS, MODULE_DOC);
+ #endif

    ...
}



@@
type mod_init_fn.T;
identifier mod_init_fn.FN;
expression E;
@@
T FN(void) {
   ...
-  if (E) return;
+  if (E) return MOD_ERROR_VAL;
   ...
}

@@
type mod_init_fn.T;
identifier mod_init_fn.FN;
identifier mod_init_fn.MOD_VAR;
@@
T FN(void) {
   ...
-  return;
+ #if PY_MAJOR_VERSION >= 3
+  return MOD_VAR;
+ #endif
}
