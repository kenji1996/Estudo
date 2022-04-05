def fatorial(m):
    n = m
    if n>1:
        m *= fatorial(m-1)
    elif n == 0:
        return 1
    return m

while True:
    m,n = input().split()
    m,n = int(m),int(n)
    print(fatorial(m)+fatorial(n))
