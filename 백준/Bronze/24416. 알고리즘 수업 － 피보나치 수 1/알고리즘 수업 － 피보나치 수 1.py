def fib(n):
    f = [1,1]
    count = 0
    for i in range(2,n):
        f.append(f[i-1] + f[i-2])
        count += 1
    return f[-1]
    
def fibonacci(n):
    count = 0
    for i in range(2,n):
        count += 1
    return count

n = int(input())
print(fib(n),fibonacci(n))