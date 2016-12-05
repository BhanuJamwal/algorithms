import math

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
sum1=0
sum2=0
for i in range(n):
        sum1=a[i][i]+sum1
        sum2=a[n-i-1][i]+sum2
print abs(sum1-sum2)