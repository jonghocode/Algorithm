n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()
answer = 0
for i in range(n):
    if answer > lst[i][0]:
        answer += lst[i][1]
    else:
        answer = lst[i][0] + lst[i][1]
print(answer)