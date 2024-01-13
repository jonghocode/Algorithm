r, M = 31, 1234567891
n = int(input())
s = input()
cnt, answer = 0, 0
for i in s:
    num = ord(i) - ord('a') + 1
    answer += num*(r**cnt)
    cnt += 1
print(answer%M)