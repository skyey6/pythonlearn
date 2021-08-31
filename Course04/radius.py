"""
输入半径计算圆的周长和面积
"""
import math

radius = float(input("输入圆的半径："))

c = 2 * math.pi * radius
s = math.pi * radius * radius

print(f"周长：{c:.2f}, 面积：{s:.2f}")
