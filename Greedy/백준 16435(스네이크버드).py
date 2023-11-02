n, l = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
answer = 0
for i in lst:
    if i <= l:
        l += 1
        answer += 1

print(l)