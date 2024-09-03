def primecheck(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
m = int(input())

for i in range(n,m):
    if primecheck(i):
        print(i)