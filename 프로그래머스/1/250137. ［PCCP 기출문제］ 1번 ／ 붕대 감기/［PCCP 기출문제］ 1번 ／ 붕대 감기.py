def solution(bandage, health, attacks):
    # 예외 1 체력 회복 시 최대 체력을 넘어선 경우
    # 예외 2 몬스터의 마지막 공격전에 체력이 0 이하가 된 경우

    continue_success = 0 # 연속 성공
    current_health = health # 현재 체력
    casting_time, heal_per_second,  plus_heal = bandage
    attack_second = [attack_time[0] for attack_time in attacks]
    attack = False
    
    for second in range(1, attack_second[-1]+1):
        if second in attack_second:
            attack = True
            current_health -= attacks[attack_second.index(second)][1] # 데미지 입음
            continue_success = 0
        else:
            attack = False
            current_health += heal_per_second # 초당 회복
            if continue_success == casting_time:
                current_health += plus_heal # 추가 회복
                continue_success = 0
            if current_health > health:
                current_health = health # 체력 보정
            
                
        continue_success += 1
        
        if current_health <= 0:
                return -1
    
    return current_health