import random
import sys


def test1(param1):
    print('test1')
    r = random.randint(1, 100)
    print(f'number generated is {r}')
    assert r < param1


if __name__ == '__main__':
    param1 = int(sys.argv[1])
    print('hello there')
    print(f'param is {param1}')
    print('begin tests')
    test1(param1)
    print('finished tests')
