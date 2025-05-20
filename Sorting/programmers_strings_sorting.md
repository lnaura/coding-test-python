from pathlib import Path

markdown_content = """
## 📌 [프로그래머스] 문자열 내 마음대로 정렬하기 (Python)

### 📝 문제 설명
문자열로 구성된 리스트 `strings`와 정수 `n`이 주어졌을 때,  
각 문자열의 **n번째 인덱스 문자**를 기준으로 오름차순 정렬하되,  
**n번째 문자가 같으면 사전 순으로 정렬**한 결과를 반환하는 문제입니다.

---

### ✅ 입력
- `strings`: 길이 1 이상 1,000 이하의 문자열 리스트 (각 문자열은 소문자)
- `n`: 0 이상 문자열 길이 미만의 정수

### ✅ 출력
- 정렬된 문자열 리스트를 반환

---

### 💡 접근 방법
1. 먼저 사전순 정렬 (`sort()`)을 수행 → n번째 문자가 같을 때를 대비
2. 이후 `key=lambda x: x[n]`을 사용해 n번째 문자 기준으로 정렬
3. 파이썬의 정렬은 **안정 정렬**이므로, 이전 정렬 결과가 유지됨

---

### 💻 코드
```python
def solution(strings, n):
    answer = []

    strings.sort()
    strings.sort(key=lambda x: x[n])

    for i in strings:
        answer.append(i)

    return answer
