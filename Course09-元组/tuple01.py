"""
元组的定义和常用操作
"""
# 定义一个三元组
t1 = (68, 45, 2)
# 定义一个四元组
t2 = ('John', 6, True, 2.2)

# 查看变量的类型
print(type(t1), type(t2))    # <class 'tuple'> <class 'tuple'>
# 查看元组中元素的数量
print(len(t1), len(t2))      # 3 4

# 通过索引运算获取元组中的元素
print(t1[0], t1[-3])         # 68 68
print(t2[3], t2[-1])         # 2.2 2.2

# 循环遍历元组中的元素
for item in t2:
    print(item)

# 成员运算
print(100 in t1)    # False
print(2.2 in t2)    # True

# 拼接
t3 = t1 + t2
print(t3)          # (68, 45, 2, 'John', 6, True, 2.2)

# 切片
print(t3[::3])     # (68, 'John', 2.2)

# 比较运算
print(t1 == t3)    # False
print(t1 >= t3)    # False
print(t1 < (69, 11, 55))    # True
