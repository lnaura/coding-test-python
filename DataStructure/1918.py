expression = input()

result = []
stack = []

priority = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0  # 스택 안에서의 우선순위는 가장 낮음
}

for i in expression:
    if i.isupper():     # 영어는 결과에 넣기
        result.append(i)
        continue
    
    if not stack:       # 수식이 스택에 없으면 넣기
        stack.append(i)
        continue

    if i == "(":        # 수식이 ( 이면 일단 넣기
        stack.append(i)
        continue
    
    if i == ")":        # 닫은 괄호가 나오면 ( 나올 때까지 수식 빼기
        while stack[-1] != "(":
            a = stack.pop()
            result.append(a)
        stack.pop()     # 괄호도 빼기
        continue

    if priority[stack[-1]] < priority[i]:   # 우선순위가 현재가 높으면 넣기
        stack.append(i)
        
    else:
        while bool(stack) and (priority[stack[-1]] >= priority[i]): # 우선순위가 낮으면 높아질 때까지 넣기
            a = stack.pop()
            result.append(a)
        stack.append(i)
        

while stack:
    a = stack.pop()
    result.append(a)

print("".join(result))
###############################################
expression = input()
result = ""  # 💡 리스트 대신 문자열에 바로 더해도 된다
stack = []

priority = {
    '*': 2, '/': 2,
    '+': 1, '-': 1,
    '(': 0
}

for token in expression:
    # 1. 피연산자인 경우
    if token.isalpha(): # isupper() 보다 범용적
        result += token

    # 2. 여는 괄호인 경우
    elif token == '(':
        stack.append(token)

    # 3. 닫는 괄호인 경우
    elif token == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop() # '(' 제거

    # 4. 그 외 연산자인 경우
    else:
        # 스택의 top이 현재 연산자보다 우선순위가 높거나 같으면 계속 pop
        while stack and priority[stack[-1]] >= priority[token]:
            result += stack.pop()
        stack.append(token) # 이후 현재 연산자를 push

# 스택에 남은 연산자 모두 pop
while stack:
    result += stack.pop()

print(result)