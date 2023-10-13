from itertools import permutations
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    else:
        return True

    
def solution(numbers):
    answer = set()
    for i in range(1,len(numbers)+1):
        perm_comb = set(map(int,map(''.join, permutations(numbers,i))))
        for j in perm_comb:
            if is_prime(j):
                answer.add(j)
    return len(answer)