def solution(survey, choices):
    answer=''
    personality = {}
    for i in 'RTCFJMAN':
        personality[i] = 0          # 성격 해시 만들기
    score = [0,3,2,1,0,1,2,3]       # 점수 리스트 만들기
    
    for i in range(len(choices)):
        if choices[i] <= 3:
            personality[survey[i][0]] += score[choices[i]]
        elif choices[i] >= 5:
            personality[survey[i][1]] += score[choices[i]]
    answer += 'RT'[personality['R']<personality['T']]
    answer += 'CF'[personality['C']<personality['F']]
    answer += 'JM'[personality['J']<personality['M']]
    answer += 'AN'[personality['A']<personality['N']]
    return answer