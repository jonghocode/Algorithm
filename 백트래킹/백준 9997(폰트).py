<<<<<<< HEAD
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
=======
def back(d, idx):
    global n, answer
    
    for i in range(26):
        if chk[i] == 0:
            return

    answer += 1

    for i in range(idx, n):
        for j in range(len(word[i])):
            chk[ord(word[i][j])-97] -= 1
        back(d+1, i+1)
        for j in range(len(word[i])):
            chk[ord(word[i][j])-97] += 1


n = int(input())
word, chk = [input() for _ in range(n)], [0 for _ in range(26)]
answer = 0

for i in range(n):
    for j in word[i]:
        chk[ord(j)-97] += 1

>>>>>>> 356b5e313915412dbe7746965ec0e26565027b00

back(0, 0)
print(answer)