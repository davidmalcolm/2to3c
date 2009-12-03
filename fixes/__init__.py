import os
import tempfile
from subprocess import Popen, PIPE

class Fix(object):
    def transform(self, string):
        raise NotImplementedError

class CoccinelleError(RuntimeError):
    def __init__(self, p, args, stderr):
        self.p = p
        self.args = args
        self.stderr = stderr

    def __str__(self):
        return ('Return code: %s (args: %s)\n --- start of captured stderr ---\n%s--- enf of captured stderr ---\n'
                % (self.p.returncode, repr(self.args), self.stderr))

class CocciFix(Fix):
    def __init__(self, filename):
        self.filename = filename

    def get_script_path(self):
        return os.path.join('fixes', self.filename)

    def transform(self, string):
        # spatch seems to require the input and output to be actual files,
        # rather than stdin/stdout.

        (src_hn, src_path) = tempfile.mkstemp(suffix="-%s.in.c" % self.filename)
        #print (src_hn, src_path)
        (dst_hn, dst_path) = tempfile.mkstemp(suffix="-%s.out.c" % self.filename)
        #print (dst_hn, dst_path)
        os.write(src_hn, string)

        args = ['spatch', '-sp_file', self.get_script_path(), src_path, '-o', dst_path]
        p = Popen(args, stdout=PIPE, stderr=PIPE)
        (stdout, stderr) = p.communicate()
        if p.returncode != 0:
            raise CoccinelleError(p, args, stderr)

        string = open(dst_path, 'r').read()
        os.close(src_hn)
        os.close(dst_hn)

        return string

import unittest
class NonequalStrings(Exception):
    def __init__(self, actual_result, exp_result):
        self.actual_result = actual_result
        self.exp_result = exp_result

    def __str__(self):
        from difflib import unified_diff
        result = '\n'
        for line in unified_diff(self.exp_result.splitlines(),
                                 self.actual_result.splitlines(), 
                                 fromfile = 'Expected result',
                                 tofile = 'Actual result',
                                 lineterm=''):
            result += line + '\n'
        return result

class FixTest(unittest.TestCase):
    '''Subclass of TestCase for verifying that a Fix is working as expected'''
    def assertTransformsTo(self, fixer, src, exp_result):
        actual_result = fixer.transform(src)
        if actual_result != exp_result:
            raise NonequalStrings(actual_result, exp_result)
            
