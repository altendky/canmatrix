from past.builtins import basestring
import sys

PY3 = sys.version_info[0] >= 3

if PY3:
    str = bytes.decode
    unicode_type = str
    basestring = str
    xrange = range
    int_types = (int,)
    long = int

    def iteritems(d):
        return iter(list(d.items()))
    def itervalues(d):
        return iter(list(d.values()))
else:
    # Python 2
    str = unicode_type = str
    basestring = basestring
    xrange = xrange
    int_types = (int, int)
    long = int

    def iteritems(d):
        return iter(d.items())
    def itervalues(d):
        return iter(d.values())
