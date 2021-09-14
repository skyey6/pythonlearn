import keyword
import math


def foo(args):
    if args is not None:
        print(args)


if __name__ == '__main__':
    print(keyword.kwlist)
    print(len(keyword.kwlist))
    foo('hello,world!')

    a = 1
    print(id(a))
    a = 10
    print(id(a))

    a = [1, 2, 3]
    print(id(a))
    b = a
    print(id(b))
    a[0] = 0
    print(b)

    x, y, z = 1, 2, 'string'  # 多元赋值
    print(x, y, z)
    x, y = y, x
    print(x, y)

    print(3/2, 3/2.0, 10/3, 10/3.0, 1/3.0, 1/3)

    y = list(range(10))
    print(y)
    print(y[1:5])  # [1,5)
    print(y[:-1])

    print(math.pi)
    print('%f' % math.pi)
    print('%20f' % math.pi)
    print('%-20f' % math.pi)
    print('%.20f' % math.pi)
    print('%.5s' % 'Guido van Rossum')

    print(list(range(10, 0, -2)))
