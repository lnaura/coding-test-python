n = int(input())
li = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    li1 = [age, name, i]
    li.append(li1)

li.sort(key = lambda x: (x[0], x[2]))

for i in range(n):
    print(li[i][0], li[i][1])
