s = input()
t = input()

while len(s) != len(t):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[::-1]
        t = t[1:]

for i in range(len(s)):
    if s[i] != t[i]:
        print(0)
        break
print(1)