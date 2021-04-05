import random


def test1(param1):
    r = random.randint(100)
    print(f'number generated is {r}')
    assert r < param1


def test2(param1):
    r = random.randint(200)
    print(f'number generated is {r}')
    assert r < param1


if __name__ == '__main__':
    param1 = sys.argv[1]
    print('hello there')
    print(f'param is {param1}')
    print('begin tests')
    test1(param1)
    test2(param1)
