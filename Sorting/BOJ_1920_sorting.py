
import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))  # 리스트 → set

m = int(input())
b = list(map(int, input().split()))

for i in b:
    print(1 if i in a else 0)

