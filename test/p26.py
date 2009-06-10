def foo():
    while (yield 'Give me a cookie') != 'cookie':
        pass
    yield 'Thank you.'

g = foo()
print g.next()
print g.send('no cookie for you')
print g.send('ok, cookie')
print g.send('cookie')
