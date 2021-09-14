"""
使用sys模块的getsizeof函数来检查保存相同元素的元组和列表各占用了多少内存空间;
使用timeit模块的timeit函数来看看创建保存相同元素的元组和列表各花费的时间。
"""
import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a))  # 450060
print(sys.getsizeof(b))  # 400028

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
