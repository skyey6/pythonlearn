"""
猜数字游戏
"""
import random

num = random.randint(1, 100)  # 产生一个1-100范围的随机数
count = 0

while True:
    your_num = int(input("输入你的数字："))
    count += 1
    if your_num == num:
        print("答案正确！")
        break
    elif your_num > num:
        print("大了")
    else:
        print("小了")
print(f"一共猜了{count}次")