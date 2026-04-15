h = 0
leap = 1

from math import sqrt

for n in range(101, 201):
    k = int(sqrt(n))
    
    for i in range(2, k + 1):
        if n % i == 0:
           leap = 0
           break
    if leap == 1:
        print ('%-4d' % n)
        h += 1
        if h % 10 == 0:
            print('')
    leap = 1
print ('The total is %d' % h)