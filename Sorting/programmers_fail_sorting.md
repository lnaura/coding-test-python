## 📌 [프로그래머스] 실패율 (Python)

### 📝 문제 설명
전체 스테이지 개수 `N`과 사용자들이 현재 멈춰있는 스테이지 번호가 담긴 리스트 `stages`가 주어집니다.  
각 스테이지에 대해 **실패율**을 구하고, 이를 기준으로 **스테이지 번호를 내림차순 정렬**하여 리턴하는 문제입니다.

- **실패율** = (스테이지에 도달했으나 클리어하지 못한 사람 수) / (스테이지에 도달한 사람 수)
- 스테이지에 도달한 유저가 없다면 실패율은 0으로 정의

---

### ✅ 입력
- `N`: 전체 스테이지 수 (1 ≤ N ≤ 500)
- `stages`: 사용자들의 현재 스테이지 (1 이상 N+1 이하, 길이 1 이상 200,000 이하)

### ✅ 출력
- 실패율이 높은 스테이지부터 내림차순으로 정렬한 스테이지 번호 리스트 반환

---

### 💡 내가 작성한 풀이
```python
def solution(N, stages):
    answer = []
    user = len(stages)
    li1 = []

    for i in range(1, N+1):
        user_cnt = 0
        user_s = 0
        # 각 스테이지를 통과한 사람 수
        for stage in stages:
            if stage > i:
                user_cnt += 1
            elif stage == i:
                user_s += 1

        if user_s == 0 :
            fail = 0
        else:
            fail = user_s / user

        user = user_cnt

        li = [i, fail]  # 스테이지 번호, 실패율 저장
        li1.append(li)

    li1.sort(key=lambda x: x[1], reverse=True)

    for i in range(N):
        answer.append(li1[i][0])

    return answer
```

#### 🔍 설명
- 각 스테이지마다 `stage == i`와 `stage > i` 조건으로 실패율 계산
- 변수명 간결하게 정리 가능 (예: `user_cnt`, `user_s` → 더 명확하게 분리 가능)

---

### ✅ 개선된 최적 풀이
```python
def solution(N, stages):
    result = []
    total_users = len(stages)

    for i in range(1, N + 1):
        current = stages.count(i)

        if total_users == 0:
            fail = 0
        else:
            fail = current / total_users

        result.append((i, fail))
        total_users -= current

    result.sort(key=lambda x: x[1], reverse=True)
    return [stage for stage, _ in result]
```

#### 🔍 개선 포인트
- `stages.count(i)`를 사용해 `i` 스테이지에 머문 사람 수 직접 구함
- 실패율 계산 후 `total_users`에서 해당 인원을 제외 (다음 스테이지 도달자 계산)
- 코드 간결성 및 가독성 향상

---

### ✅ 비교 요약

| 항목 | 내가 작성한 코드 | 추천 개선 코드 |
|------|------------------|----------------|
| 정확성 | ✅ | ✅ |
| 성능 | 보통 (O(NM)) | 보통 (O(NM)) |
| 가독성 | 보통 (변수명, 중복 정렬 있음) | ✅ 더 깔끔 |

---

### 📘 예시
```python
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# 결과: [3, 4, 2, 1, 5]
```

실패율:
- 1번: 1/8
- 2번: 3/7
- 3번: 2/4
- 4번: 1/2
- 5번: 0/1

---