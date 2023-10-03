s = input()
t = input()

while len(s) != len(t):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[::-1]
        t = t[1:]

if s!=t:
    print(0)
else:
    print(1)