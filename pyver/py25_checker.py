### TODO: Fill in this plugin.

from logilab import astng

from pylint.interfaces import IASTNGChecker
from pylint.checkers import BaseChecker
from pylint.checkers.utils import safe_infer

class Python25Checker(BaseChecker):
    """Check for language/library features which were added in Python 2.6."""

    __implements__ = IASTNGChecker

    name = 'py25'
    msgs = {
    }
    options = ()

##############################
# Language features
#
#       'with'
#       from __future__ import print_function
#       from __future__ import unicode_literals
#       class decorators
#       __dir__ implementations

##############################
# New modules
#
#       multiprocessing
#       future_builtins
#       io
#       abc
#       numbers
#       fractions
#       ast
#       json
#       plistlib
#       ssl

##############################
# New classes
#
#       Callable
#       Container
#       Hashable
#       ItemsView
#       Iterable
#       Iterator
#       KeysView
#       Mapping
#       MappingView
#       MutableMapping
#       MutableSequence
#       MutableSet
#       Sequence
#       Set
#       Sized
#       ValuesView
#       Queue.PriorityQueue
#       Queue.LifoQueue
#       smtplib.SMTP_SSL
#       tempfile.SpooledTemporaryFile

##############################
# New methods
#
#       str.format
#       tuple.count
#       tuple.index
#       float.hex
#       float.fromhex
#       itertools.chain.from_iterable
#       mmap.mmap.rfind
#       random.Random.triangular
#       subprocess.Popen.terminate
#       subprocess.Popen.kill
#       subprocess.Popen.send_signal
#       zipfile.ZipFile.extract
#       zipfile.ZipFile.extractall

##############################
# New functions
#
#       namedtuple
#       __builtin__.next
#       math.isinf
#       math.isnan
#       math.copysign
#       math.factorial
#       math.fsum
#       math.acosh
#       math.asinh
#       math.atanh
#       math.log1p
#       math.trunc
#       cmath.polar
#       cmath.rect
#       cmath.phase
#       cmath.isnan
#       cmath.isinf
#       functools.reduce
#       heapq.merge
#       heapq.heappushpop
#       itertools.izip_longest
#       itertools.product
#       itertools.combinations
#       itertools.permutations
#       operator.methodcaller
#       os.fchmod
#       os.fchown
#       os.lchmod
#       os.chflags
#       os.lchflags
#       os.closerange
#       os.path.relpath
#       pickletools.optimize
#       pkgutil.get_data
#       random.triangular
#       shutil.ignore_patterns
#       signal.set_wakeup_fd
#       signal.siginterrupt
#       signal.getitimer
#       signal.setitimer
#       socket.create_connection
#       sys.getsizeof
#       warnings.catch_warnings

##############################
# New attributes
#
#       stat.UF_APPEND
#       stat.UF_IMMUTABLE
#       stat.UF_NODUMP
#       stat.UF_NOUNLINK
#       stat.UF_OPAQUE
#       sys.float_info
#       sys.dont_write_bytecode
#       sys.flags

##############################
# New arguments
#
#       set.intersection                            (more than one arg)
#       set.intersection_update                     (more than one arg)
#       set.union                                   (more than one arg)
#       set.update                                  (more than one arg)
#       set.difference                              (more than one arg)
#       set.difference_update                       (more than one arg)
#       deque.__init__                              (maxlen arg)
#       logging.FileHandler.__init__                (delay arg)
#       logging.WatchedFileHandler.__init__         (delay arg)
#       logging.RotatingFileHandler.__init__        (delay arg)
#       logging.TimedRotatingFileHandler.__init__   (delay arg)
#       logging.TimedRotatingFileHandler.__init__   (utc arg)
#       mmap.mmap.find                              (end arg)
#       os.walk                                     (followlinks arg)
#       shutil.copytree                             (ignore arg)
#       smtplib.SMTP                                (timeout arg)
#       tarfile.open                                (encoding arg)
#       tarfile.open                                (errors arg)
#       urllib.urlopen                              (timeout arg)
#       urllib.ftpwrapper.__init__                  (timeout arg)
#       urllib2.urlopen                             (timeout arg)
#       warnings.formatwarning                      (line arg)
#       warnings.showwarning                        (line arg)
#       SimpleXMLRPCServer.SimpleXMLRPCServer       (bind_and_activate arg)
#       DocXMLRPCServer.DocXMLRPCServer             (bind_and_activate arg)

def register(linter):
    """required method to auto register this checker"""
    linter.register_checker(Python25Checker(linter))

