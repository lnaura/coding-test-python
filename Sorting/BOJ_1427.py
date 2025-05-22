n = input()  # 문자열로 입력받기
digits = list(n)  # 각 자리수를 리스트로 변환
digits.sort(reverse=True)  # 내림차순 정렬

print(''.join(digits))  # 리스트를 문자열로 이어서 출력