# 1541 잃어버린 괄호

s = input()
answer = 0
num = ''
sw = 0
for i in range(len(s)):
    if s[i] != '-' and s[i] != '+':
        num += s[i]
    else:
        if sw == 1:
            answer -= int(num)
        else:
            answer += int(num)
        if s[i] == '-':
            sw = 1
        num = ''

if sw == 1:
    answer -= int(num)
else:
    answer += int(num)
print(answer)