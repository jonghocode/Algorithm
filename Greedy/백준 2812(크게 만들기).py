# 스택이 비어있거나 key값보다 작거나 같으면 넣기
# 자기보다 낮으면 앞에거 다 빼기 k개 동안

n, k = map(int, input().split())
num = list(map(int, input()))
stack, cnt = [], 0

for i in num:
    if len(stack) == 0 or stack[-1] >= i or cnt == k:
        stack.append(i)
    else:
        for j in range(len(stack)-1, -1, -1):
            if len(stack) == 0 or stack[j] >= i or cnt == k:
                break
            stack.pop()
            cnt+=1
        stack.append(i)

if len(stack) != n-k:
    while True:
        if len(stack) == n-k:
            break
        stack.pop()

print(''.join(map(str,stack)))