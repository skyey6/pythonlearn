items = ['Python', 'Java', 'Go', 'Kotlin']

# 使用append方法在列表 尾部 添加元素
items.append('Swift')
print(items)  # ['Python', 'Java', 'Go', 'Kotlin', 'Swift']

# 使用insert方法在列表指定索引位置插入元素
items.insert(2, 'SQL')
print(items)  # ['Python', 'Java', 'SQL', 'Go', 'Kotlin', 'Swift']

# 删除指定的元素
items.remove('Java')
print(items)  # ['Python', 'SQL', 'Go', 'Kotlin', 'Swift']

# 删除指定索引位置的元素
s1 = items.pop(0)
s2 = items.pop(len(items) - 1)
print('removed items:', s1, s2)  # removed items: Python Swift
print(items)  # ['SQL', 'Go', 'Kotlin']

print(items.index('Go'))

# 清空列表中的元素
items.clear()
print(items)  # []
