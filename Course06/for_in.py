"""
用for循环实现1~100求和
"""

total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050

"""
用for循环实现1~100之间的偶数求和
"""
total = 0
for i in range(1, 101, 2):
    total += i
print(total)  # 2500
