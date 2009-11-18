@@
expression E1;
@@
-PyInt_AsLong(E1)
+PyLong_AsLong(E1)

@@
expression E1;
@@
-PyInt_Check(E1)
+PyLong_Check(E1)

@@
expression E1, E2, E3;
@@
-PyInt_FromString(E1, E2, E3)
+PyLong_FromString(E1, E2, E3)

@@
expression E1, E2, E3;
@@
-PyInt_FromUnicode(E1, E2, E3)
+PyLong_FromUnicode(E1, E2, E3)

@@
expression E1;
@@
-PyInt_FromLong(E1)
+PyLong_FromLong(E1)

@@
expression E1;
@@
-PyInt_FromSize_t(E1)
+PyLong_FromSize_t(E1)

@@
expression E1;
@@
-PyInt_FromSsize_t(E1)
+PyLong_FromSsize_t(E1)

@@
expression E1;
@@
-PyInt_AsLong(E1)
+PyLong_AsLong(E1)

@@
expression E1;
@@
-PyInt_AsSsize_t(E1)
+PyLong_AsSsize_t(E1)

@@
expression E1;
@@
-PyInt_AsUnsignedLongMask(E1)
+PyLong_AsUnsignedLongMask(E1)

@@
expression E1;
@@
-PyInt_AsUnsignedLongLongMask(E1)
+PyLong_AsUnsignedLongLongMask(E1)

@@
expression E1;
@@
-PyInt_AS_LONG(E1)
+PyLong_AS_LONG(E1)

@@
expression E1;
@@
-PyNumber_Int(E1)
+PyNumber_Long(E1)
