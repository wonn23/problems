def list_slice(s, num):
    rlist = []
    mock = len(s) // num
    namuji = len(s) % num
    for i in range(1, mock + 1):
        rlist.append(s[num * (i - 1) : num * i])

    if namuji:
        rlist.append(s[len(s) - namuji :])

    return rlist


def solution(s):
    # 1씩 증가하면서 문자를 잘라본다.
    # 자른 문자열을 앞뒤로 비교한다.
    # 비교했을때 같은 수만큼 숫자를 써준다.
    # 전체 문자열의 길이를 return한다.
    # 인덱스 증가폭을 활용한다면?
    # 일단 앞뒤 문자가 같을 때, 숫자를 생략하는 알고리즘 만들기
    # 마지막 3c 를 어떻게 추가할 것인가?
    answer = []
    for i in range(1, len(s) + 1):
        string_list = list_slice(s, i)
        count = 1
        result = ""
        for index in range(1, len(string_list)):
            if string_list[index - 1] == string_list[index]:
                count += 1
            else:
                if count == 1:
                    result += string_list[index - 1]
                    count = 1
                else:
                    result += str(count) + string_list[index - 1]
                    count = 1
        if count == 1:
            result += string_list[-1]
        else:
            result += str(count) + string_list[-1]
        answer.append(len(result))
    return min(answer)