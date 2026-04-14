user_name = []  # 用来存放排序后的 3 个数

# 先输入第一个数，直接放进列表
num = int(input("Please enter some numbers: "))
user_name.append(num)

# 再输入第二个数
num = int(input("Please enter some numbers: "))
user_name.append(num)

# 让列表保持从小到大
if user_name[0] > user_name[1]:
    user_name[0], user_name[1] = user_name[1], user_name[0]

# 输入第三个数，并插入到正确位置（核心逻辑）
num = int(input("Please enter some numbers: "))

if num <= user_name[0]:
    user_name.insert(0, num)
elif num <= user_name[1]:
    user_name.insert(1, num)
else:
    user_name.append(num)

# 输出结果
print(user_name)