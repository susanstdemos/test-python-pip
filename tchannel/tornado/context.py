from __future__ import absolute_import

gcontext = None

class Context(object):
    def __init__(self):
        self.parent_tracing = None
    def __enter__(self):
        print 'enter'
        global gcontext
        self._old_context = gcontext
        gcontext = self
    def __exit__(self, type, value, traceback):
        print 'exit'
        global gcontext
        gcontext = self._old_context
