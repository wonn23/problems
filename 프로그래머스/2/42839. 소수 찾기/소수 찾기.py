import math
import itertools
def is_prime_num(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = int(math.sqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    num = list(numbers)
    prime_set = set()
    for i in range(1, len(num) + 1):
        result = ''
        a = list(itertools.permutations(num, i))
        for j in a:
            # 튜플 안의 문자열을 합치기
            combined = ''.join(j)
            # 합친 문자열을 숫자로 변환
            number = int(combined)
            if is_prime_num(number):
                prime_set.add(number)
        print(prime_set)
    answer = len(prime_set)
    return answer