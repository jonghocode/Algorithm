n = int(input())
lst = []
for i in range(1, n+1):
    lst.append(i)

while True:
    print(lst.pop(0), end=' ')
    if not lst:
        break
    lst.append(lst.pop(0))
     