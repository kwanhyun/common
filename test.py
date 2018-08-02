from contextlib import contextmanager
@contextmanager

def myopen(filepath, mode, encode):
    f = open(filepath, mode, encoding=encode)
    try:
        yield f # with절의 as에 넘겨집니다.
    finally:
        f.close()
with myopen('helloworld.txt', 'wt', 'utf8') as f:
    f.write('hello')
    f.write('world')