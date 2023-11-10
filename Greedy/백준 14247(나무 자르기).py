n = int(input())
lst = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = []
for i in range(n):
    lst3.append([lst[i], lst2[i]])
lst3.sort(key = lambda x : x[1])
answer = 0

for i in range(n):
    answer += lst3[i][0] + lst3[i][1]*i
print(answer)