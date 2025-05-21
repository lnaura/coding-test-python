import sys

n = int(sys.stdin.readline())
words = list(set(sys.stdin.readline().strip() for _ in range(n)))

# 먼저 사전순, 그 다음 길이순으로 정렬
words.sort()  # 먼저 사전순
words.sort(key=lambda x: len(x))  # 그다음 길이순 (안정 정렬이므로 사전순 유지됨)

for word in words:
    print(word)

