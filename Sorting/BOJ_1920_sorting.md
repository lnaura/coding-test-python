# 백준 1920번 - 수 찾기

## 📝 문제 설명

- N개의 정수로 이루어진 집합 A가 주어진다.
- M개의 수가 주어졌을 때, 이 수들이 집합 A에 존재하는지 각각 확인하는 문제.

🔗 [문제 링크](https://www.acmicpc.net/problem/1920)

---

## ✅ 문제 조건 요약

- **입력**
  - 첫 줄: 정수 N (1 ≤ N ≤ 100,000)
  - 둘째 줄: 집합 A를 이루는 N개의 정수
  - 셋째 줄: 정수 M (1 ≤ M ≤ 100,000)
  - 넷째 줄: 확인할 M개의 정수

- **출력**
  - 각 수가 A에 존재하면 1, 아니면 0을 출력

---

## ⚠️ 시간 초과 주의

### ❌ 잘못된 접근: 리스트에서 탐색

```python
for i in b:
    if i in a:        # 리스트에서 탐색은 O(N)
        print(1)
    else:
        print(0)
```

- `i in a`는 리스트를 처음부터 끝까지 검색 → **O(N)**
- 이를 M번 반복 → 전체 시간 복잡도 **O(N × M)** → 시간 초과 발생 가능

---

## ✅ 해결 방법: `set` 자료구조 활용

- 파이썬의 `set`은 해시 테이블 기반 → 평균적으로 `in` 연산이 **O(1)**

---

## 💡 정답 코드 (Python)

```python
import sys
input = sys.stdin.readline

n = int(input())
a = set(map(int, input().split()))  # 리스트 → set

m = int(input())
b = list(map(int, input().split()))

for i in b:
    print(1 if i in a else 0)
```

---

## 📚 핵심 요약

| 기능 | 잘못된 방식 | 올바른 방식 |
|------|--------------|----------------|
| 탐색 | `x in list` → O(N) | `x in set` → O(1) |
| 전체 시간복잡도 | O(N × M) | O(N + M) |
| 입력 최적화 | `input()` | `sys.stdin.readline()` |

- ✅ 탐색은 반드시 `set` 사용
- ✅ 빠른 입력 처리로 시간 초과 방지
- ✅ 조건문 출력 형식 주의

---
