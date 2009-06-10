from logilab import astng

from pylint.interfaces import IASTNGChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import safe_infer

# 2.4->2.5 issues we do not presently detect:
#    1. try-except-finally seems undetectable in pylint!
#    2. 'yield' as expression, not statement (can crash pylint!)

class Python24Checker(BaseChecker):
    """Check for language/library features which were added in Python 2.5."""

    __implements__ = IASTNGChecker

    name = 'py24'
    msgs = {
            'W8400': ('Conditional expressions were introduced in 2.5',
                        'Used when a conditional expression is found.'),
            'W8401': ("'from __future__ import absolute_import introduced in 2.5",
                        'Used when absolute_import is imported from __future__.'),
            'W8402': ("'from __future__ import with_statement introduced in 2.5",
                        'Used when with_statement is imported from __future__.'),
            'W8403': ("'__index__ method had no special meaning before 2.5",
                        'Used when method __index__ is defined on a class.'),
            'W8404': ("'__missing__ method had no special meaning before 2.5",
                        'Used when method __missing__ is defined on a class.'),
            'W8405': ("str.startswith may only be called with a tuple in 2.5+",
                        'Used when str.startswith is called with a tuple rather than a string.'),
            'W8406': ("str.endsswith may only be called with a tuple in 2.5+",
                        'Used when str.endsswith is called with a tuple rather than a string.'),
            'W8407': ("operator.itemgetter may only be called with multiple arguments in 2.5+",
                        'Used when operator.itemgetter is called with multiple arguments.'),
            'W8408': ("operator.attrgetter may only be called with multiple arguments in 2.5+",
                        'Used when operator.attrgetter is called with multiple arguments.'),
    }
    options = ()

    BAD_MODULES = {
            'functools':                                        'W8410',
            'runpy':                                            'W8411',
            'contextlib':                                       'W8412',
            'cProfile':                                         'W8413',
            'msilib':                                           'W8414',
            'spwd':                                             'W8415',
            'uuid':                                             'W8416',
            'ctypes':                                           'W8417',
            'xml.etree':                                        'W8418',
            'hashlib':                                          'W8419',
            'sqlite3':                                          'W8420',
            'wsgiref':                                          'W8421',
    }
    for k, v in BAD_MODULES.items():
        msgs[v] = (("The '%s' module was introduced in 2.5" % k),
                   ("Used when the '%s' module is imported." % k))

    BAD_FUNCTIONS = {
            ('__builtin__', 'any'):                             'W8430',
            ('__builtin__', 'all'):                             'W8431',
            ('gc',          'get_count'):                       'W8432',
            ('locale',      'format_string'):                   'W8433',
            ('locale',      'currency'):                        'W8434',
            ('os',          'wait3'):                           'W8435',
            ('os',          'wait4'):                           'W8436',
            ('posix',       'wait3'):                           'W8435',
            ('posix',       'wait4'):                           'W8436',
            ('sys',         '_current_frames'):                 'W8437',
            ('threading',   'stack_size'):                      'W8438',
            ('thread',      'stack_size'):                      'W8438',
            ('webbrowser',  'open_new'):                        'W8439',
            ('webbrowser',  'open_new_tab'):                    'W8440',
            ('csv',         'field_size_limit'):                'W8441',
            ('_csv',        'field_size_limit'):                'W8441',
    }
    for k, v in BAD_FUNCTIONS.items():
        if k[0] == 'posix' or k[0] == 'thread' or k[0] == '_csv':
            continue
        if k[0] == '__builtin__':
            msgs[v] = (("The '%s' builtin function was introduced in 2.5" % k[1]),
                       ("Used when the '%s' builtin function is called." % k[1]))
        else:
            msgs[v] = (("The '%s.%s' function was introduced in 2.5" % k),
                       ("Used when the '%s.%s' function is called." % k))

    BAD_CLASSES = {
            ('collections', 'defaultdict'):                     'W8450',
            ('mailbox',     'mbox'):                            'W8451',
            ('mailbox',     'MH'):                              'W8452',
            ('mailbox',     'Maildir'):                         'W8453',
    }
    for k, v in BAD_CLASSES.items():
        msgs[v] = (("The '%s.%s' class was introduced in 2.5" % k),
                   ("Used when the '%s.%s' class is referenced or instantiated." % k))

    BAD_METHODS = {
            ('optparse.OptionParser',       'destroy'):         'W8460',
            ('Queue.Queue',                 'join'):            'W8461',
            ('Queue.Queue',                 'task_done'):       'W8462',
            ('socket.socket',               'recv_into'):       'W8463',
            ('socket.socket',               'recvfrom_into'):   'W8464',
            ('socket._socketobj',           'recv_into'):       'W8463',
            ('socket._socketobj',           'recvfrom_into'):   'W8464',
            ('_socket.socket',              'recv_into'):       'W8463',
            ('_socket.socket',              'recvfrom_into'):   'W8464',
            ('__builtin__.str',             'partition'):       'W8465',
            ('__builtin__.str',             'rpartition'):      'W8466',
            ('collections.deque',           'remove'):          'W8467',
            ('datetime.datetime',           'strptime'):        'W8468',
            ('tarfile.TarFile',             'extractall'):      'W8469',
            ('weakref.WeakKeyDictionary',   'iterkeyrefs'):     'W8470',
            ('weakref.WeakKeyDictionary',   'keyrefs'):         'W8471',
            ('weakref.WeakValueDictionary', 'itervaluerefs'):   'W8472',
            ('weakref.WeakValueDictionary', 'valuerefs'):       'W8473',
    }
    BAD_METHOD_CLASSES = []
    for k, v in BAD_METHODS.items():
        if k[0] == 'socket._socketobj' or k[0] == '_socket.socket':
            continue
        if k[0].startswith('__builtin__'):
            k = (k[0][12:], k[1])
        msgs[v] = (("The '%s.%s' method was introduced in 2.5" % k),
                   ("Used when the '%s' method is called on an object of type '%s'." % (k[1], k[0])))
        BAD_METHOD_CLASSES.append(k[0])

    BAD_ATTRIBUTES = {
            ('optparse.OptionParser',       'epilog'):          'W8475',
            ('os',                          'SEEK_SET'):        'W8476',
            ('os',                          'SEEK_CUR'):        'W8477',
            ('os',                          'SEEK_END'):        'W8478',
            ('os',                          'O_SHLOCK'):        'W8479',
            ('os',                          'O_EXLOCK'):        'W8480',
            ('SimpleXMLRPCServer.SimpleXMLRPCServer', 'rpc_paths'): 'W8481',
            ('DocXMLRPCServer.DocXMLRPCServer', 'rpc_paths'):   'W8482',
            ('sys',                         'subversion'):      'W8483',
            ('socket._socketobj',           'family'):          'W8484',
            ('socket._socketobj',           'type'):            'W8485',
            ('socket._socketobj',           'proto'):           'W8486',
            ('socket.socket',               'family'):          'W8484',
            ('socket.socket',               'type'):            'W8485',
            ('socket.socket',               'proto'):           'W8486',
            ('_socket.socket',              'family'):          'W8484',
            ('_socket.socket',              'type'):            'W8485',
            ('_socket.socket',              'proto'):           'W8486',
    }
    for k, v in BAD_ATTRIBUTES.items():
        if k[0] == 'socket._socketobj' or k[0] == '_socket.socket':
            continue
        msgs[v] = (("The '%s.%s' attribute was introduced in 2.5" % k),
                   ("Used when the '%s' attribute is accessed on an object of type '%s'." % (k[1], k[0])))

    BAD_ARGUMENTS = {
            ('heapq',       'nsmallest', 'key'):                'W8490',
            ('heapq',       'nlargest',  'key'):                'W8491',
            ('__builtin__', 'min',       'key'):                'W8492',
            ('__builtin__', 'max',       'key'):                'W8493',
            ('nis',         'match',     'domain'):             'W8494',
            ('nis',         'maps',      'domain'):             'W8495',
            ('webbrowser',  'open',      'autoraise'):          'W8496',
    }
    for k, v in BAD_ARGUMENTS.items():
        mod, func, arg = k
        msgs[v] = (("The keyword argument '%s' to the function '%s.%s' was introduced in 2.5" % (arg, mod, func)),
                   ("Used when the '%s.%s' function is called with the keyword argument %s." % k))

    BAD_ATTRIBUTES.update(BAD_METHODS)
    BAD_ATTRIBUTES.update(BAD_FUNCTIONS)
    BAD_ATTRIBUTES.update(BAD_CLASSES)

    def visit_from(self, node):
        if node.modname == '__future__':
            for k, _ in node.names:
                if k == 'absolute_import':
                    self.add_message('W8401', line=node.lineno)
                elif k == 'with_statement':
                    self.add_message('W8402', line=node.lineno)
        elif node.modname in self.BAD_MODULES:
            self.add_message(self.BAD_MODULES[node.modname], line=node.lineno)
        else:
            for n, _ in node.names:
                childname = node.modname + '.' + n
                if childname in self.BAD_MODULES:
                    self.add_message(self.BAD_MODULES[childname], line=node.lineno)

    def visit_import(self, node):
        for k, _ in node.names:
            if k in self.BAD_MODULES:
                self.add_message(self.BAD_MODULES[k], line=node.lineno)

    def visit_ifexp(self, node):
        self.add_message('W8400', line=node.lineno)

    def visit_callfunc(self, node):
        inferred = safe_infer(node.func)
        if inferred is not None:
            if isinstance(inferred, astng.Function):
                key = (inferred.parent.frame().qname(), inferred.name)
                # Find unqualified function calls
                if not isinstance(node.func, astng.Getattr) and key in self.BAD_FUNCTIONS:
                    self.add_message(self.BAD_FUNCTIONS[key], line=node.lineno)
                if node.args is not None:
                    for arg in node.args:
                        if isinstance(arg, astng.Keyword):
                            newkey = key + (arg.arg,)
                            if newkey in self.BAD_ARGUMENTS:
                                self.add_message(self.BAD_ARGUMENTS[newkey], line=node.lineno)
            elif isinstance(inferred, astng.Class):
                key = (inferred.parent.frame().qname(), inferred.name)
                if key in self.BAD_CLASSES:
                    self.add_message(self.BAD_CLASSES[key], line=node.lineno)
                if key == ('operator', 'itemgetter'):
                    children = list(node.get_children())
                    if len(children) > 2:
                        self.add_message('W8407', line=node.lineno)
                elif key == ('operator', 'attrgetter'):
                    children = list(node.get_children())
                    if len(children) > 2:
                        self.add_message('W8408', line=node.lineno)
            elif isinstance(inferred, astng.UnboundMethod):
                key = (inferred.parent.frame().qname(), inferred.name)
                if key == ('__builtin__.str', 'startswith'):
                    if isinstance(node.args[0], astng.Tuple):
                        self.add_message('W8405', line=node.lineno)
                elif key == ('__builtin__.str', 'endswith'):
                    if isinstance(node.args[0], astng.Tuple):
                        self.add_message('W8406', line=node.lineno)

    def visit_getattr(self, node):
        inferred_expr = safe_infer(node.expr)
        if inferred_expr is not None:
            if isinstance(inferred_expr, astng.Module):
                key = (inferred_expr.qname(), node.attrname)
            else:
                key = (inferred_expr.pytype(), node.attrname)
            if key in self.BAD_ATTRIBUTES:
                self.add_message(self.BAD_ATTRIBUTES[key], line=node.lineno)

    def visit_function(self, node):
        if not node.is_method():
            return
        if node.name == '__index__':
            self.add_message('W8403', line=node.lineno)
        elif node.name == '__missing__':
            self.add_message('W8404', line=node.lineno)

    # XXX: bad class uses which don't involve construction?
    # XXX: calls of bad methods on subclasses?

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(Python24Checker(linter))

