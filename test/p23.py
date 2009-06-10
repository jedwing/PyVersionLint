"""Test case for Python 2.3 lint."""

for a in (x for x in range(200) if (x & 1)):
    print a

s = set()
fs = frozenset()
l = reversed([1, 2, 3, 4])

a = 'abcde'
a.ljust(10, ' ')
a.rjust(10, ' ')
a.center(10, ' ')
a.ljust(10)
a.rjust(10)
a.center(10)
a.rsplit('.')

a = [1, 2, 3, 4]
a.sort()
a.sort(key=lambda x: -x)
a.sort(cmp=lambda x, y: y<x)
a.sort(reverse=True)
a.sort(key=lambda x: -x, reverse=True)
a.sort(cmp=lambda x, y: y<x, reverse=True)
a.sort(key=lambda x: -x, cmp=lambda x, y: y<x)
a.sort(key=lambda x: -x, cmp=lambda x, y: y<x, reverse=True)

a = list(sorted([4, 3, 2, 1]))

import asyncore
asyncore.loop(count=100)

import string
t = string.Template('$name: $value')
t.substitute({'name': 'Boo', 'value': 'Hamster'})

import subprocess
from subprocess import Dracula
import subprocess as sp
from subprocess import Dracula as Vlad

import decimal
from decimal import Dracula
import decimal as sp
from decimal import Dracula as Vlad

@foobar
def foofunc():
    pass
