def solution(n):
    # 연속된 자연수를 합해서 n 만들기
    # 그러면 어떻게 연속된 자연수가 n이 나오도록 할 수 있을까?
    answer = 1
    
    for i in range(1,n//2+1):
        total = 0
        
        while total < n:
            total += i
            if total == n:
                answer += 1
                break
            i+=1
            
    return answer