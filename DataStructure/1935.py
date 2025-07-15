n = int(input())
expression = input()
operand_values = {} # 값을 저장할 딕셔너리
stack = []

for i in range(n):
    alphabet = chr(ord('A') + i)
    num = int(input()) # 피연산자에 해당하는 숫자 입력
    operand_values[alphabet] = num

for s in expression:
    if s.isupper():
        stack.append(operand_values[s])
    else:
        num2 = stack.pop()
        num1 = stack.pop()

        result = 0
        if s == '+':
            result = num1 + num2
        elif s == '-':
            result = num1 - num2
        elif s == '*':
            result = num1 * num2
        elif s == '/':
            result = num1 / num2
        stack.append(result)

print(f"{stack.pop():.2f}")

