from logilab import astng

from pylint.interfaces import IASTNGChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import safe_infer

# 2.3->2.4 issues we do not presently detect:
#    1. dict.update can take any sequence of (k, v), not just dictionaries.
#    2. some more esoteric issues (eval, execfile 'locals' parameter; zip behavior on empty list...)
#
# Note: These checks can be made a bit better, I think, by using some of the
# code I added to the 2.4->2.5 checker...

class Python23Checker(BaseChecker):
    """Check for language/library features which were added in Python 2.4."""

    __implements__ = IASTNGChecker

    name = 'py23'
    msgs = {
            'W8301': ('Generator expressions were introduced in 2.4',
                        ('Used when a generator expression is found.')),
            'W8302': ('set was introduced in 2.4',
                        ('Used when a set object is constructed.')),
            'W8303': ('frozenset was introduced in 2.4',
                        ('Used when a frozenset object is constructed.')),
            'W8304': ('reversed was introduced in 2.4',
                        ('Used when a reversed sequence is constructed.')),
            'W8305': ('Decorators were introduced in 2.4',
                        ('Used when a function or method decorator is used.')),
            'W8306': ("Second arg to 'ljust', 'rjust', and 'center' was introduced in 2.4",
                        ('Used when two-argument form of str.ljust/rjust/center are called.')),
            'W8307': ("str.rsplit was introduced in 2.4",
                        ('Used when str.rsplit is called.')),
            'W8308': ("keyword arguments to sort were introduced in 2.4",
                        ('Used when list.sort is called with keyword arguments.')),
            'W8309': ("sorted was introduced in 2.4",
                        ("Used when the 'sorted' builtin function is called.")),
            'W8310': ("string.Template and string.SafeTemplate were introduced in 2.4",
                        ("Used when the string.Template or string.SafeTemplate class is used.")),
            'W8311': ("subprocess module was introduced in 2.4",
                        ("Used when the subprocess module is imported.")),
            'W8312': ("decimal module was introduced in 2.4",
                        ("Used when the decimal module is imported.")),
            'W8313': ("collections module was introduced in 2.4",
                        ("Used when the collections module is imported.")),
            'W8314': ("'count' parameter to asyncore.loop was introduced in 2.4",
                        ("Used when asyncore.loop is called with a 'count' keyword argument.")),
    }
    options = ()

    def visit_decorators(self, node):
        self.add_message('W8305', line=node.lineno)

    def visit_from(self, node):
        if node.modname == 'subprocess' \
                or node.modname.startswith('subprocess.'):
            self.add_message('W8311', line=node.lineno)
        elif node.modname == 'decimal' \
                or node.modname.startswith('decimal.'):
            self.add_message('W8312', line=node.lineno)
        elif node.modname == 'collections' \
                or node.modname.startswith('collections.'):
            self.add_message('W8313', line=node.lineno)

    def visit_import(self, node):
        for k, v in node.names:
            if k == 'subprocess' or k.startswith('subprocess.'):
                self.add_message('W8311', line=node.lineno)
            elif k == 'decimal' or k.startswith('decimal.'):
                self.add_message('W8312', line=node.lineno)
            elif k == 'collections' or k.startswith('collections.'):
                self.add_message('W8313', line=node.lineno)

    def visit_callfunc(self, node):
        inferred = safe_infer(node.func)
        if inferred is not None:
            # print inferred, inferred.parent.frame().qname(), inferred.name
            if isinstance(inferred, astng.Class):
                if inferred.parent.frame().qname() == '__builtin__':
                    if inferred.name == 'set':
                        self.add_message('W8302', line=node.lineno)
                    elif inferred.name == 'frozenset':
                        self.add_message('W8303', line=node.lineno)
                    elif inferred.name == 'reversed':
                        self.add_message('W8304', line=node.lineno)
                if inferred.parent.frame().qname() == 'string':
                    if inferred.name == 'Template' or inferred.name == 'SafeTemplate':
                        self.add_message('W8310', line=node.lineno)
            elif isinstance(inferred, astng.Function):
                if inferred.parent.frame().qname() == '__builtin__':
                    if inferred.name == 'sorted':
                        self.add_message('W8309', line=node.lineno)
                elif inferred.parent.frame().qname() == 'asyncore':
                    if inferred.name == 'loop':
                        for ch in node.get_children():
                            if isinstance(ch, astng.Keyword) and ch.arg == 'count':
                                self.add_message('W8314', line=node.lineno)
            elif isinstance(inferred, astng.UnboundMethod):
                children = list(node.get_children())
                if inferred.parent.frame().qname() == '__builtin__.str':
                    if inferred.name in ['ljust', 'rjust', 'center']:
                        if len(children) > 2:
                            self.add_message('W8306', line=node.lineno)
                    elif inferred.name == 'rsplit':
                        self.add_message('W8307', line=node.lineno)
                elif inferred.parent.frame().qname() == '__builtin__.list':
                    if inferred.name == 'sort':
                        if len(children) > 1:
                            self.add_message('W8308', line=node.lineno)

    def visit_genexpr(self, node):
        """called when a GenExpr node is encountered. See compiler.ast
        documentation for a description of available nodes:
        http://www.python.org/doc/current/lib/module-compiler.ast.html
        )
        """
        self.add_message('W8301', line=node.lineno)

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(Python23Checker(linter))

