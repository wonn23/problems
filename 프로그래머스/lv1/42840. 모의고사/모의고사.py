def solution(answers):
    answer = []
    num1 = [1,2,3,4,5] * 2000
    num2 = [2,1,2,3,2,4,2,5] * 1250
    num3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    num1_answer = 0
    num2_answer = 0
    num3_answer = 0
    for i in range(len(answers)):
        if num1[i] == answers[i]:
            num1_answer +=1
        if num2[i] == answers[i]:
            num2_answer +=1
        if num3[i] == answers[i]:
            num3_answer +=1
    max_num = max(num1_answer,num2_answer,num3_answer)
    if max_num == num1_answer:
        answer.append(1)
    if max_num == num2_answer:
        answer.append(2)
    if max_num == num3_answer:
        answer.append(3)    
               
    return answer