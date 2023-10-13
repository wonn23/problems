import math
def solution(brown, yellow):
    area = brown + yellow
    for i in range(1,int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            h = i
            w = yellow // h
            
            if (w+2) * (h+2) == area:
                return [w+2,h+2]