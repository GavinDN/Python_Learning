user_salary = int(input("Please enter your salary: "))

arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
r = 0

for idx in range(0, 6):
    if user_salary > arr[idx]:
        r += (user_salary - arr[idx]) * rat[idx]
        print((user_salary - arr[idx]) * rat[idx])
        user_salary = arr[idx]
print(r)