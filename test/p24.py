"""This module is designed to contain all of the features which were not
present in Python 2.4 but present in 2.5.  It's a test case for the Pylint
plugin I'm writing."""

from __future__ import absolute_import
from __future__ import with_statement

import operator
from gc import get_count
import locale, os, sys, threading, webbrowser, csv
from collections import defaultdict
from mailbox import mbox
import mailbox
from optparse import OptionParser
from Queue import Queue
import socket
import collections
import datetime
import tarfile
import weakref
import SimpleXMLRPCServer
import DocXMLRPCServer
import heapq
from nis import match, maps

#pylint: disable-msg=W0611
import functools
#pylint: disable-msg=W0611
import runpy
#pylint: disable-msg=E0611,F0401
import runpy.iguana
#pylint: disable-msg=F0401
import contextlib, cProfile, msilib
#pylint: disable-msg=W0611
import spwd, uuid
#pylint: disable-msg=W0611
import ctypes
#pylint: disable-msg=W0611
import xml.etree
#pylint: disable-msg=W0611
from xml import etree
#pylint: disable-msg=W0611
from hashlib import md5
#pylint: disable-msg=W0611
import sqlite3, wsgiref

#pylint: disable-msg=R0903
class TestClass(object):
    """This class defines the 'special' methods __index__ and __missing__,
    which were not special before 2.5."""
    def __index__(self):
        pass
    def __missing__(self):
        pass

'abcdef'.startswith(('a', 'b', 'c'))
'abcdef'.endswith(('a', 'b', 'c'))
VAR0 = 'abcdef'
VAR0.startswith(('a', 'b', 'c'))
VAR0.endswith(('a', 'b', 'c'))

operator.itemgetter('a', 'b')
operator.attrgetter('a', 'b')

VAR0 = any([x < 10 for x in range(20)])
VAR1 = all([x < 10 for x in range(20)])
VAR2 = get_count()
VAR3 = locale.format_string('abcdef')
VAR4 = locale.currency(123.45)
VAR5 = os.wait3('')
VAR6 = os.wait4('', 123)
#pylint: disable-msg=W0212
VAR7 = sys._current_frames()
VAR8 = threading.stack_size()
VAR9 = webbrowser.open_new('http://www.nytimes.com')
VAR10 = webbrowser.open_new_tab('http://www.nytimes.com')
VAR11 = csv.field_size_limit()

DDICT = defaultdict(list)
MBOX0 = mbox()
MBOX1 = mailbox.MH()
MBOX2 = mailbox.Maildir()

OP0 = OptionParser()
OP1 = Queue()
OP2 = socket.socket()
OP3 = 'abcdef'
OP4 = collections.deque()
OP5 = datetime.datetime(1976, 6, 21)
OP6 = tarfile.TarFile()
OP7 = weakref.WeakKeyDictionary()
OP8 = weakref.WeakValueDictionary()
print OP0.destroy()
print OP1.join()
print OP1.task_done()
print OP2.recv_into('')
print OP2.recvfrom_into('', '')
print OP3.partition('c')
print OP3.rpartition('c')
print OP4.remove(1)
print OP5.strptime('%p-%v')
print OP6.extractall()
print OP7.iterkeyrefs()
print OP7.keyrefs()
print OP8.itervaluerefs()
print OP8.valuerefs()

AP1 = OP0
AP2 = os
AP3 = SimpleXMLRPCServer.SimpleXMLRPCServer()
AP4 = DocXMLRPCServer.DocXMLRPCServer()
AP5 = sys
AP6 = OP2
print AP1.epilog
print AP2.SEEK_SET, AP2.SEEK_CUR, AP2.SEEK_END
#pylint: disable-msg=E1101
print AP2.O_SHLOCK, AP2.O_EXLOCK
#pylint: disable-msg=E1101
print AP3.rpc_paths
#pylint: disable-msg=E1101
print AP4.rpc_paths
print AP5.subversion
print AP6.family
print AP6.type
print AP6.proto

print heapq.nsmallest(1, ['a', 'b'], key=lambda x: 'your mom')
print heapq.nlargest(1, ['a', 'b'], key=lambda x: 'your mom')
print min([], key=lambda x: 'your mom')
print max([], key=lambda x: 'your mom')
print match('foo', domain='lalala')
print maps('foo', domain='lalala')
webbrowser.open(autoraise=True)

######### This is not detectable using pylint machinery, I think.
# try:
#     print 'foo'
# except IOError, e:
#     print 'bar'
# else:
#     print 'baz'
# finally:
#     print 'zoinks'

######### This crashes pylint, so...  no.
# def generator_func():
#     while (yield 'Give me a cookie') != 'cookie':
#         pass
# g = foo()
# g.next()
# g.send('no cookie for you')
# g.send('ok, cookie')
# g.send('cookie')

ZED = 'a' if 1 < 2 else 'b'
