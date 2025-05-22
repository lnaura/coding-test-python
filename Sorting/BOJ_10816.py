from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
sang = list(map(int, input().split()))

m = int(input())
li = list(map(int, input().split()))

count = Counter(sang)

for x in li:
    print(count[x], end=' ')
