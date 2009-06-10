def foo():
    while (yield 'Give me a cookie') != 'cookie':
        pass

g = foo()
g.next()
g.send('no cookie for you')
g.send('ok, cookie')
g.send('cookie')
