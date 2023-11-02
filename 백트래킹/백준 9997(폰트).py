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


back(0, 0)
print(answer)