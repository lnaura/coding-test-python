
## 📌 [백준 10814] 나이순 정렬 (Python)

### 📝 문제 설명
온라인 저지에 가입한 사람들의 나이와 이름이 주어졌을 때,  
**나이순으로 오름차순 정렬**하되,  
**나이가 같으면 가입한 순서(입력 순서)**를 유지하여 정렬하는 문제입니다.

---

### ✅ 입력
- 첫째 줄에 회원 수 N (1 ≤ N ≤ 100,000)
- 둘째 줄부터 N개의 줄에 `나이 이름`이 주어짐  
  (이름은 알파벳 대소문자로 이루어지며 길이 ≤ 100)

### ✅ 출력
- 조건에 따라 정렬된 회원 정보를 출력 (각 줄에 나이와 이름)

---

### 💡 내가 작성한 풀이
```python
n = int(input())
li = []

for i in range(n):
    age, name = input().split()
    age = int(age)
    li.append([age, name, i])  # 입력 순서 i 저장

li.sort(key=lambda x: (x[0], x[2]))  # 나이 → 입력순 정렬

for i in range(n):
    print(li[i][0], li[i][1])
```
---
### 🔎 설명
- 나이 기준 정렬하고, 나이가 같을 경우 입력 순서대로 정렬되도록 i를 추가로 저장

- 정확히 작동하지만 Python에서는 입력 순서를 직접 저장하지 않아도 됨

---
### ✅ 더 깔끔하고 효율적인 방법 (추천)
```py
n = int(input())
li = []

for _ in range(n):
    age, name = input().split()
    li.append((int(age), name))

li.sort(key=lambda x: x[0])  # 나이 기준만 정렬

for age, name in li:
    print(age, name)
```
---
### 🔎 이유
- Python의 sort()는 안정 정렬 → 나이가 같으면 입력 순서 유지됨

- 따라서 입력 순서를 따로 저장하지 않아도 조건을 만족함

- 코드가 더 간단하고 가독성 높음