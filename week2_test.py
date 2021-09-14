import copy

if __name__ == '__main__':
    list1 = list(range(1, 10))
    print(list1)     # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(list1[3:8])   # [4, 5, 6, 7, 8]
    print(list1[3:-1])  # [4, 5, 6, 7, 8]
    print(list1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    d = {}
    d['names'] = ['Alfred', 'Bertrand']
    c = d.copy()
    dc = copy.deepcopy(d)
    d['names'].append('Clive')
    print(c)
    print(dc)

    a, b, c, d, e = 20, 10, 15, 5, 0
    e = (a+b)*c/d
    print(e)