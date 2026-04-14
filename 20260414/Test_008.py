def sum(n):
    for i in range(1, n):
        print()
        for j in range(1, i + 1):
            print("%d * %d = %d" % (i, j, i * j), end = " ")

sum(10)