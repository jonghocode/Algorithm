n = int(input())
a, b, c = 300, 60, 10
an, bn, cn = 0, 0, 0

if n >= a:
    an = n//a
    n = n%a
if n >= b:
    bn = n//b
    n = n%b
if n >= c:
    cn = n//c
    n = n%c

if n != 0:
    print(-1)
else:
    print(an, bn, cn)