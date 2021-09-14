"""
遍历列表的方式
"""
items = ['Python', 'Java', 'Go', 'Kotlin']

# 方式1
for item in items:
    print(item, end='\t')

print()
# 方式2
for i in range(len(items)):
    print(items[i], end='\t')
