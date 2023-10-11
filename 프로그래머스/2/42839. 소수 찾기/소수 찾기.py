import math
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    
    prime_set = set()
    
    for i in range(1, len(num_list) + 1):
        perm_comb = permutations(num_list, i)
        
        for perm in perm_comb:
            num_str = ''.join(perm)
            num_int = int(num_str)
            
            if is_prime(num_int) and num_int not in prime_set:
                prime_set.add(num_int)
                answer += 1
    
    return answer
