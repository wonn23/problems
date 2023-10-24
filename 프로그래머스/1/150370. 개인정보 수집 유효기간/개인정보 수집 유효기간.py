from datetime import datetime, timedelta
def convet_to_int(date_str):
        return list(map(int,date_str.split("."))) # "2022.05.19" -> [2022, 5, 19]
    
    
def solution(today, terms, privacies):
    
    obj = {} 
    for term in terms:
        alpha, duration = term.split()
        obj[alpha] = int(duration) # {A: 6, B: 12, C: 3}

        
    number = 1  # 파기할 개인 정보 번호
    answer = [] # 파기할 번호 리스트
    today = convet_to_int(today)    # [2022, 5, 19]
    for i in privacies:
        # 개인정보 수집 일자에 유효기간을 더해서 날짜 계산하기
        date, alpha = i.split()     # ["2021.05.02 A", "A"]
        date = convet_to_int(date)  # [2021, 5, 2]
        year, month, day = date
        
        month += obj[alpha]  # 유효기간을 달에 더해준다.

        # 제한 사항에서 유효기간은 1~100이라고 나와있다.
        year += month//12 # year와 month 순서 바뀌면 답이 틀림
        
        month %= 12       # 12월에서 12월을 더하면 month // 12 = 2가 되고 month % 12 = 0이 된다. 
        if month == 0:
            month = 12
            year -= 1

        # today와 유효기간을 더한 개인 정보 수집일자를 비교해서
        # today > 유효기간을 더한 개인 정보 수집일자이면 파기하기
        if today[0] > year:
            answer.append(number)
        elif today[0] == year and today[1] > month:
            answer.append(number)
        elif today[0] == year and today[1] == month and today[2] >= day:
            answer.append(number)
        print(today, year, month, day, number)
        number += 1
    return answer