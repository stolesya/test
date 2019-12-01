#3*5
#[[0 for j in range(m)] for i in range(n)]
import sys
import random
col=3
row=5
arr=[[random.randint(0, 9) for j in range(col)] for i in range(row)]
print(arr)

sum=0
mul=1
count0=0
for i in range(row):
    for j in range(col):
        el=arr[i][j]
        sys.stdout.write(str(el))
        sum+=el
        if el!=0: 
            mul*=el
        else:
            count0+=1
    print()
print(sum, mul, count0)