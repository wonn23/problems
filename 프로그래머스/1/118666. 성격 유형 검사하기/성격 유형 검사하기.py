def solution(survey, choices):
    answer=''
    personality = {}
    for i in 'RTCFJMAN':
        personality[i] = 0          # 성격 해시 만들기
    print(personality)
    score = [0,3,2,1,0,1,2,3]       # 점수 리스트 만들기
    
    for i in range(len(choices)):
        if choices[i] <= 3:
            personality[survey[i][0]] += score[choices[i]]
        elif choices[i] >= 5:
            personality[survey[i][1]] += score[choices[i]]
    print(personality)
    answer += 'RT'[personality['R']<personality['T']] # 'RT'[True]
    answer += 'CF'[personality['C']<personality['F']] # 'CF'[False]
    answer += 'JM'[personality['J']<personality['M']] # 'CM'[True]
    answer += 'AN'[personality['A']<personality['N']] # 'AN'[False]
    return answer