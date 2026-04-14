# 输入要算到第几个月
month = int(input("Please enter month: "))

a = 1
b = 1

if month < 1:
    print("输入错误")

if month >= 1:
    print("第1个月，兔子有 %d 对" % a)
    print("第2个月，兔子有 %d 对" % b)

    # 从第3个月开始循环计算
    for i in range(3, month + 1):
        c = a + b    # 当月 = 前两个月之和
        a = b        # 往前挪一个月
        b = c        # 往前挪一个月
        print(f"第{i}个月：{c} 对")

print(f"\n第{month}个月总共有：{b} 对兔子")