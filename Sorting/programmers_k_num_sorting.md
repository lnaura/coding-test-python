## 📌 [프로그래머스] K번째 수 (Python)

### 📝 문제 설명
주어진 배열 `array`에서, 각 명령어 `commands`를 수행합니다.  
각 명령어는 `[i, j, k]` 형식이며, `array[i-1]`부터 `array[j-1]`까지 자른 후 정렬하여, 정렬된 배열에서 `k번째` 수를 구하는 문제입니다.

### ✅ 입력
- `array`: 1 이상 100 이하의 정수로 이루어진 배열
- `commands`: `[i, j, k]` 형태의 명령어를 담은 배열

### ✅ 출력
- 각 명령어에 따라 구한 결과값들을 순서대로 담은 배열

---

### 💡 접근 방법
- `commands`를 하나씩 순회하면서, 
  - `array[i-1:j]` 범위를 슬라이싱하고
  - 해당 슬라이스를 정렬한 후
  - `k-1`번째 인덱스 값을 결과 리스트에 추가
- 인덱스는 0부터 시작하는 점을 유의!

---

### 💻 코드
```python
def solution(array, commands):
    answer = []

    for li in commands:
        i, j, k = li
        li1 = []
        for n in range(i-1, j):
            li1.append(array[n])
        li1.sort()
        answer.append(li1[k-1])

    return answer

# 예시 입력
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))  # [5, 6, 3]
```

---

### 📌 기타
- 리스트 슬라이싱과 정렬을 이해하기 좋은 문제
- Python의 `sorted()` 또는 리스트 슬라이싱 문법으로 더 간결하게 작성할 수도 있음