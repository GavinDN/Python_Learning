salary_line = [100000, 200000, 400000, 600000, 1000000]
rat = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

while True:
    profit = int(input("Please enter profit: "))
    bonus = 0

    if profit <= 100000:
        bonus = profit * 0.1

    elif profit <= 200000:
        bonus = 100000*0.1 + (profit-100000)*0.075

    elif profit <= 400000:
        bonus = 100000*0.1 + 100000*0.075 + (profit-200000)*0.05

    elif profit <= 600000:
        bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + (profit-400000)*0.03

    elif profit <= 1000000:
        bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + (profit-600000)*0.015

    else:
        bonus = 100000*0.1 + 100000*0.075 + 200000*0.05 + 200000*0.03 + 400000*0.015 + (profit-1000000)*0.01

    print("Total bonus: " + str(bonus))