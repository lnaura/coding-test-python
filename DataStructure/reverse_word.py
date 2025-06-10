T = int(input())

for i in range(T):
    words = list(input().split())

    for word in words:
        w = list(word)
        for k in range(len(w)-1,-1,-1):
            print(w[k], end = "")
        print(end=' ')
    print()


