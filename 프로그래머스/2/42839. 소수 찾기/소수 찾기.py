from itertools import permutations
import math
def solution(numbers):
    numbers_list = list(numbers)
    result = []
    
    for i in range(len(numbers_list)+1):
        result = result + list(permutations((numbers_list),i))
    result = set(result)
    
    new_list = []
    for i in result:
        is_decial = ""
        for j in i:
            is_decial += j
        if i and int(is_decial) >= 2:
            new_list.append(int(is_decial))
    
    answer = 0
    for i in set(new_list):
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:    
            answer += 1
    return answer