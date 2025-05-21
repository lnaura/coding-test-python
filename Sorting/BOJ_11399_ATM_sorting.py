

n = int(input())
t = list(map(int,input().split()))

t.sort()

result = 0
s_result = 0
for i in t:
    result += i 
    s_result += result

print(s_result)