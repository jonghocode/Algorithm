n = int(input())
t = [1, 1, 2, 5]
for i in range(4, 36):
    sum = 0
    for j in range(i):
        sum += t[j]*t[i-j-1]
    t.append(sum)
print(t[n])