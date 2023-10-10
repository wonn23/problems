def solution(answers):
    answer = []
    give_up1 = [1,2,3,4,5] * 2000
    give_up2 = [2,1,2,3,2,4,2,5] * 1250
    give_up3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    counts = []
    count1 = count2 = count3 = 0
    
    for index, num in enumerate(answers):
        if num == give_up1[index]:
            count1 += 1
        if num == give_up2[index]:
            count2 += 1
        if num == give_up3[index]:
            count3 += 1
    
    counts.append((1,count1))
    counts.append((2,count2))
    counts.append((3,count3))
    
    counts.sort(key = lambda x: x[1],reverse = True)
    if counts[2][1] == counts[0][1]:
        return sorted([counts[0][0],counts[1][0],counts[2][0]])
    elif counts[1][1] == counts[0][1]:
        return sorted([counts[0][0],counts[1][0]])
        
    return [counts[0][0]]