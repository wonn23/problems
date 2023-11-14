def solution(skill, skill_trees):
    # 스킬을 순서대로 확인하는 방법은? -> 인덱스 비교를 통해 확인한다.
    # 상관 없는 스킬은 어떻게 지나치지? -> 그냥 if 문 하나 더 만들어 준다.
    skill_index = {} # { "C": 0, "B": 1, "D": 2 }
    for index, s in enumerate(skill):
        skill_index[s] = index
        
    count = 0
    for skill_tree in skill_trees:
        order_index = 0
        for s in skill_tree: # 배열 내에 있는 스킬 트리를 하나씩 돈다.
            if s not in skill: # skill 내에 없는 스킬이면 for문을 계속 돈다. 
                continue
                
            if order_index == skill_index[s]: # 순서를 맞추기 위해서 order_index는 순서대로 1씩 증가해야 한다.
                order_index += 1
            else: # skill_index와 order_index가 다르다면 for문을 멈춘다
                break
        
        else: # for문을 이상없이 돌았다면 count += 1 한다.
            count += 1
    return count