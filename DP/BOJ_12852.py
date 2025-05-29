n = int(input())

d = [0] * 1000001
prev = [0] * 1000001
array = []
for i in range(2,n+1):
    d[i] = d[i-1] + 1
    prev[i] = i-1
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
        array.append(i//3)
        prev[i] = i // 3
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2]+1)
        prev[i] == i//2

print(d[n])
now = n
while now != 0:
    print(i, end = ' ')
    now = prev[now]