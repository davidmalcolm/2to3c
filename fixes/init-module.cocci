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
identifier MOD_VAR;
expression MODULE_NAME, MODULE_METHODS, MODULE_DOC;
expression E;
@@
   if (E) {
-     return;
+     return MOD_ERROR_VAL;
   }
   ...
   MOD_VAR = Py_InitModule3(MODULE_NAME, MODULE_METHODS, MODULE_DOC); 


@@
identifier MOD_VAR;
expression MODULE_NAME, MODULE_METHODS, MODULE_DOC;
expression E;
@@
   MOD_VAR = Py_InitModule3(MODULE_NAME, MODULE_METHODS, MODULE_DOC); 
   ...
   if (E) {
-     return;
+     return MOD_ERROR_VAL;
   }


@@
type mod_init_fn.T;
identifier  mod_init_fn.FN;
identifier  mod_init_fn.MOD_VAR;
expression MODULE_NAME, MODULE_METHODS, MODULE_DOC;
expression E;
statement list SL;
@@
+struct __HASH_IF_PY_MAJOR_VERSION_ge_3;
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
+struct __HASH_DEFINE__MOD_ERROR_VAL__NULL;
+struct __HASH_ELSE;
+struct __HASH_DEFINE__MOD_ERROR_VAL__;
+struct __HASH_ENDIF;

 T FN(void) {
   ...

+__HASH_IF_PY_MAJOR_VERSION_ge_3;
+    MOD_VAR = PyModule_Create(&moduledef);
+__HASH_ELSE;
     MOD_VAR = Py_InitModule3(MODULE_NAME, MODULE_METHODS, MODULE_DOC);
+__HASH_ENDIF;

   ...
 }


