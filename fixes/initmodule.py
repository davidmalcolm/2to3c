from fixes import CocciFix, FixTest
class FixInitModule(CocciFix):
    def __init__(self):
        CocciFix.__init__(self, 'init-module.cocci')

    def preprocess(self, string):
        # FIXME
        return string

    def postprocess(self, string):
        for (before, after) in [('struct __HASH_IF_PY_MAJOR_VERSION_ge_3;',
                                 '#if PY_MAJOR_VERSION > 3'),
                                ('struct __HASH_ELSE;',
                                 '#else'),
                                ('struct __HASH_DEFINE__MOD_ERROR_VAL__NULL;',
                                 '#define MOD_ERROR_VAL NULL'),
                                ('struct __HASH_DEFINE__MOD_ERROR_VAL__;',
                                 '#define MOD_ERROR_VAL'),
                                ('struct __HASH_ENDIF;',
                                 '#endif'),
                                ('__HASH_IF_PY_MAJOR_VERSION_ge_3;',
                                 '#if PY_MAJOR_VERSION > 3'),
                                ('__HASH_ELSE;',
                                 '#else'),
                                ('__HASH_ENDIF;',
                                 '#endif'),
                                ]:
            string = string.replace(before, after)

        # etc
        return string

    def transform(self, string):
        # FIXME: preprocess
        string = self.preprocess(string)
        #print 'input:', repr(string)
        string = CocciFix.transform(self, string)
        #print 'output:', repr(string)
        string = self.postprocess(string)
        return string

#import unittest
class TestFixups(FixTest):
    def setUp(self):
        self.fixer = FixInitModule()

    def test_fixups(self):
        self.assertTransformsTo(self.fixer,
                                '''
PyMODINIT_FUNC
initxx(void)
{
    PyObject *m;

    if (something_that_can_fail() < 0)
        return;

    m = Py_InitModule3("xx", xx_methods, module_doc);
    if (m == NULL)
        return;

    PyModule_AddObject(m, "Null", (PyObject *)&Null_Type);
}
''',
                                '''
#if PY_MAJOR_VERSION > 3
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "xx",/* m_name */
    module_doc,/* m_doc */
    0,/* m_size */
    xx_methods,/* m_methods */
    NULL,/* m_reload */
    NULL,/* m_traverse */
    NULL,/* m_clear */
    NULL,/* m_free */
};
#define MOD_ERROR_VAL NULL
#else
#define MOD_ERROR_VAL
#endif
PyMODINIT_FUNC
initxx(void)
{
    PyObject *m;

    if (something_that_can_fail() < 0)
        return MOD_ERROR_VAL;

    #if PY_MAJOR_VERSION > 3
    m = PyModule_Create(&moduledef);
    #else
    m = Py_InitModule3("xx", xx_methods, module_doc);
    #endif
    if (m == NULL)
        return MOD_ERROR_VAL;

    PyModule_AddObject(m, "Null", (PyObject *)&Null_Type);
}
''')
# FIXME: this should have a trailing:
'''
    #if PY_MAJOR_VERSION > 3
    return m;
    #endif
'''
# but I haven't figured out how to get spatch to add that whilst correctly
# handling error paths

# Some code that isn't handled yet:
# Multiple error-handling paths:
'''
PyMODINIT_FUNC
initxx(void)
{
    PyObject *m;

    if (something_that_can_fail() < 0)
        return;

    m = Py_InitModule3("xx", xx_methods, module_doc);
    if (m == NULL)
        return;

    if (PyType_Ready(&Null_Type) < 0)
        return;
    PyModule_AddObject(m, "Null", (PyObject *)&Null_Type);
}
'''

if __name__ == '__main__':
    unittest.main()
