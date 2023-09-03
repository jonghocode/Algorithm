n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

minus, plus, zero = [], [], []
answer = 0

for i in lst:
    if i == 1: # 1은 더하는 것이 더 큼
        answer += 1
    elif i > 0: # 양수는 곱하는 것이 더 큼
        plus.append(i)
    else: # 음수와 0은 서로 곱하는 것이 더 큼
        minus.append(i)

plus.sort()
minus.sort(reverse=True)

while len(plus):
    if len(plus) == 1:
        answer += plus.pop()
    else:
        answer += plus.pop() * plus.pop()

while len(minus):
    if len(minus) == 1:
        answer += minus.pop()
    else:
        answer += minus.pop() * minus.pop()

print(answer)
