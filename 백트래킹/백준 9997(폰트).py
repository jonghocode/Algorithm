def back(idx, now):
    global n, answer
    
    if 67108863 == now:
        answer += 1
    
    for i in range(idx, n):
        back(i+1, lst[i]|now)
        
n = int(input())
word = [input() for _ in range(n)]
lst = [0]*n

for i in range(n):
    for j in word[i]:
        lst[i] |= 1 <<(ord(j)-97)
print(lst)
answer = 0

back(0, 0)
print(answer)