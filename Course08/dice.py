"""
投6000次色子，记录每一面出现的次数
"""
import random

counter = [0] * 6  # 列表含有6个元素
print(counter)

for i in range(6000):
    num = random.randint(1, 6)
    counter[num - 1] += 1

print(counter)
