"""
切片操作
"""
s = 'abc123456'

# i=2, j=5, k=1的正向切片操作
print(s[2:5])       # c12

# i=-7, j=-4, k=1的正向切片操作
print(s[-7:-4])     # c12

# i=2, j=9, k=1的正向切片操作
print(s[2:])        # c123456

# i=-7, j=9, k=1的正向切片操作
print(s[-7:])       # c123456

# i=2, j=9, k=2的正向切片操作
print(s[2::2])      # c246

# i=-7, j=9, k=2的正向切片操作
print(s[-7::2])     # c246

# i=0, j=9, k=2的正向切片操作
print(s[::2])       # ac246

# i=1, j=-1, k=2的正向切片操作
print(s[1:-1:2])    # b135

# i=7, j=1, k=-1的负向切片操作
print(s[7:1:-1])    # 54321c

# i=-2, j=-8, k=-1的负向切片操作
print(s[-2:-8:-1])  # 54321c

# i=7, j=-10, k=-1的负向切片操作
print(s[7::-1])     # 54321cba

# i=-1, j=1, k=-1的负向切片操作
print(s[:1:-1])     # 654321c

# i=0, j=9, k=1的正向切片
print(s[:])         # abc123456

# i=0, j=9, k=2的正向切片
print(s[::2])       # ac246

# i=-1, j=-10, k=-1的负向切片
print(s[::-1])      # 654321cba

# i=-1, j=-10, k=-2的负向切片
print(s[::-2])      # 642ca
