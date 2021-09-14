"""
字典的运算
"""
person = {'name': '王大锤', 'age': 55, 'weight': 60}
# 检查name和tel两个键在不在person字典中
print('name' in person, 'tel' in person)    # True False
# 通过age修将person字典中对应的值修改为25
if 'age' in person:
    person['age'] = 25
print(person)   # {'name': '王大锤', 'age': 25, 'weight': 60}
# 通过索引操作向person字典中存入新的键值对
person['tel'] = '13122334455'
person['signature'] = '这个人很懒，什么也没写~'
print('name' in person, 'tel' in person)    # True True
# 检查person字典中键值对的数量
print(len(person))    # 5
# 对字典的键进行循环并通索引运算获取键对应的值
for key in person:
    print(f'{key}: {person[key]}')
