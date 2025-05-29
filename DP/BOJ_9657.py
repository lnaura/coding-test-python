n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 2
d[3] = 1
d[4] = 1


for i in range(5, n+1):
    if d[i - 1] % 2 == 1 and d[i-3] % 2 == 1 and d[i-4] % 2 == 1:
        d[i] = 2     
    else:
        d[i] = 1

if d[n] % 2 == 0:
    print("CY")
else:
    print("SK")




