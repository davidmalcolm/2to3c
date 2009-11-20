import os
import tempfile
from subprocess import Popen, PIPE

class Fix(object):
    def transform(self, string):
        raise NotImplementedError

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

        p = Popen(['spatch', '-sp_file', self.get_script_path(), src_path, '-o', dst_path], stdout=PIPE, stderr=PIPE)
        p.wait()

        string = open(dst_path, 'r').read()
        os.close(src_hn)
        os.close(dst_hn)

        return string
