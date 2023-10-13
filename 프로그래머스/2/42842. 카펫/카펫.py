def solution(brown, yellow):
    area = brown + yellow
    for i in range(1,area):
        width = area//i
        length = i
        if width+length == (brown+4)//2 and width*length == area:
            answer = [width,length]
            break
    return answer