def p(s):
    if len(s) == 1 or len(s) == 0:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return p(s[1:-1])
    

def g(k):
    for i in range(2, k):
        if k%i == 0:
            return False
    return True

n = int(input())

i = n
while True:
    if i > 14000000:
        break
    if p(str(i)) and g(i):
        print(i)
        break
    i+=1