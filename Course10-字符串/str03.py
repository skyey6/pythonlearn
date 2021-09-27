"""
拼接和重复
"""
s1 = 'hello' + ' ' + 'world'
print(s1)    # hello world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2     # s1 = s1 + s2
print(s1)    # hello world!!!
s1 *= 2      # s1 = s1 * 2
print(s1)    # hello world!!!hello world!!!
print("========================")

"""
比较运算
"""
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2, s1 < s2)      # False True
print(s2 == 'hello world')    # True
print(s2 == 'Hello world')    # False
print(s2 != 'Hello world')    # True
s3 = 'tky'
print(ord('t'), ord('k'), ord('y'))      # 116 107 121
s4 = '小王'
print(ord('小'), ord('王'))    # 23567 29579
print(s3 > s4, s3 <= s4)      # False True
