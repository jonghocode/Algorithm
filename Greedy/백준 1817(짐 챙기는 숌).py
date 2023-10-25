n, m = map(int, input().split())
answer = 0
if n != 0:
    lst = list(map(int, input().split()))
    sum = 0
    for i in lst:
        if sum + i < m:
            sum += i
        elif sum + i == m:
            sum = 0
            answer += 1
        else:
            answer += 1
            sum = i

if sum:
    answer += 1
if m == 0 or n == 0:
    answer = 0
print(answer)