def solution(n):
    result = [ i if i%2==1 else i**2 for i in range(n+1)]
    return sum(result[1::2]) if n%2==1 else sum(result[::2])