"""
转义字符和原始字符串
"""
s1 = '\'hello, world!\''
print(s1)
s2 = '\\hello, world!\\'
print(s2)

# 字符串s1中\t是制表符，\n是换行符
s1 = '\time up \now'
print(s1)
# 字符串s2中没有转义字符，每个字符都是原始含义
s2 = r'\time up \now'
print(s2)

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u7530\u5f00\u5143'
print(s1, s2)