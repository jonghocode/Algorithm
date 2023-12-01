# 오등큰수

n = int(input())
lst = list(map(int, input().split()))
dict = {}
for i in lst:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

answer = [0]*n
answer[-1] = -1
stack = [lst[-1]]

for i in range(n-2, -1, -1):
    if stack:
        if dict[stack[-1]] > dict[lst[i]]:
            answer[i] = stack[-1]
            stack.append(lst[i])
        else:
            while True:
                if len(stack) == 0 or dict[stack[-1]] > dict[lst[i]]:
                    break
                stack.pop()
            if len(stack) == 0:
                answer[i] = -1
            else:
                answer[i] = stack[-1]
            stack.append(lst[i])
    else:
        answer[i] = -1

for i in range(n):
    print(answer[i], end=' ')