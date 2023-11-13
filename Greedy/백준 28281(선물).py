n, x = map(int, input().split())
lst = list(map(int, input().split()))
sum = 0x7fffffff
for i in range(n-1):
    sum = min(sum, lst[i] + lst[i+1])
print(sum*x)