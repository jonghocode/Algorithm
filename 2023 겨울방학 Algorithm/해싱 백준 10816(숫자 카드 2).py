X = 678971

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
hash = [[] for i in range(X)]

for i in lst:
    num = i
    if num < 0:
        num *= -2
    else:
        num *= 2
    sw = 0
    for j in range(len(hash[num%X])):
        if hash[num%X][j][0] == i:
            sw = 1
            hash[num%X][j][1] += 1
    if sw == 0:
        hash[num%X].append([i, 1])


for i in find:
    num = i
    if num < 0:
        num *= -2
    else:
        num *= 2
    
    sw = 0
    for j in range(len(hash[num%X])):
        if hash[num%X][j][0] == i:
            sw = 1
            print(hash[num%X][j][1], end=' ')
            break
    if sw == 0:
        print(0, end=' ')
