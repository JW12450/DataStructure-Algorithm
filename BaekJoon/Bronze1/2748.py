def fib2(n):
    if (n==1):
        return 1
    elif (n==0):
        return 0
    else:
        return fib(n-1) + fib(n-2)

def fib(n):
    _curr, _next = 0, 1
    for _ in range(n):
        _curr, _next = _next, _curr + _next
    return _curr

n = int(input())
#재귀로 풀면 시간 초과..
print(fib(n))