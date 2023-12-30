import sys

n = int(input())
lst = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
idx = 1
p = 0
answer = []
while p < len(lst):
    if stack:
        if stack[-1] == lst[p]:
            stack.pop()
            p += 1
            answer.append('-')
        elif stack[-1] > lst[p]:
            print("NO")
            exit()
        else:
            while idx <= n:
                if stack[-1] == lst[p]:
                    break
                stack.append(idx)
                answer.append('+')
                idx += 1
    else:
        while idx <= n:
            if stack:
                if stack[-1] == lst[p]:
                    break
            stack.append(idx)
            answer.append('+')
            idx += 1

for i in answer:
    print(i)