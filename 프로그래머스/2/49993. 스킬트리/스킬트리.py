def solution(skill, skill_trees):
    skill_index = {}
    for index, s in enumerate(skill):
        skill_index[s] = index
        
    count = 0
    for skill_tree in skill_trees:
        order_index = 0
        for s in skill_tree:            
            if s not in skill:
                continue
                
            if order_index == skill_index[s]:
                order_index += 1
            else:
                break
        
        else:
            count += 1
    return count