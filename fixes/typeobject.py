import sys
import re
from difflib import unified_diff

# Whitespace patterns:
req_ws = r'\s+'
opt_ws = r'\s*'
c_identifier = r'([_A-Za-z][_0-9A-Za-z]*)'

pat = ('.*' + r'PyTypeObject' + req_ws
       + c_identifier + opt_ws 
       + r'=' + opt_ws + r'\{' + opt_ws 
       + r'(PyObject_HEAD_INIT\((.*)\)' + opt_ws 
       + r'([0-9]+)' + opt_ws + r',).*'
       )

def fixup_typeobject_initializers(content):
    while True:
        m = re.match(pat, content, re.DOTALL)
        if m:
            if False:
                print m.groups()
                print m.group(2)
                print m.group(3)
                print m.group(4)
                print m.span(2)
            content = (content[:m.start(2)] 
                       + 'PyVarObject_HEAD_INIT(%s, %s)' % (m.group(3),m.group(4))
                       + content[m.end(2):])
        else:
            return content

import unittest
class TestFixups(unittest.TestCase):
    def test_fixups(self):
        self.assertEquals(fixup_typeobject_initializers('''
PyTypeObject DBusPyIntBase_Type = {
    PyObject_HEAD_INIT(DEFERRED_ADDRESS(&PyType_Type))
    0,
    "_dbus_bindings._IntBase",
'''
                                                        ),
                          '''
PyTypeObject DBusPyIntBase_Type = {
    PyVarObject_HEAD_INIT(DEFERRED_ADDRESS(&PyType_Type), 0)
    "_dbus_bindings._IntBase",
'''
                          )


def fixup_file(filename, options):
    content = open(filename, 'r').read()        
    fixed_content = fixup_typeobject_initializers(content)
    if content != fixed_content:
        for line in unified_diff(content.splitlines(),
                                 fixed_content.splitlines(), 
                                 fromfile = filename+'.orig',
                                 tofile = filename,
                                 lineterm=''):
            print line

        if options.write:
            open(filename, 'w').write(fixed_content)

if __name__ == '__main__':
    unittest.main()
