n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
for i in range(1, len(lst)):
    lst[i-1] = lst[i]-lst[i-1]
lst.pop()
lst.sort()
answer = 0
for i in range(len(lst)-k+1):
    answer += lst[i]
print(answer)
