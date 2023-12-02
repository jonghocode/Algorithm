n = int(input())
answer = [666]
for i in range(1, n+1):
    t = i
    a = ''; b = '666'
    while True:
        if i == 10:
            print(a, b)
        if t == 0:
            break
        k = t%10
        if k > 6 or k == 0:
            b += str(k)
        else:
            a += str(k)
        t //= 10
    answer.append(int(a+b))
answer.sort()
print(answer)