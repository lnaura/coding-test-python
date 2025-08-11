from itertools import combinations
import sys

while True:
    input_data = list(map(int, sys.stdin.readline().split()))
    k = input_data[0]

    if k == 0:
        break

    s = input_data[1:]
    
    # s 리스트에서 6개를 뽑는 모든 조합을 구함
    for comb in combinations(s, 6):
        print(' '.join(map(str, comb)))
    
    print()