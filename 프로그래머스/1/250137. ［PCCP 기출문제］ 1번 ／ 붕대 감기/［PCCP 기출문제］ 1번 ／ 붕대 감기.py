def solution(bandage, health, attacks):
    time = attacks[-1][0]
    continue_success = 0
    max_health = health
    casting_time, heal_per_second,  plus_heal = bandage
    # badage = [시전 시간, 초당 회복량, 추가 회복량]
    # casting_time, heal_per_second,  plus_heal = banage
    # health = 최대 체력
    # attcks = [공격 시간, 피해량]
    # attack_time, damage
    # return 몬스터의 마지막 공격직후의 체력 or -1(체력 0이하)
    # 예외 1 체력 회복 시 최대 체력을 넘어선 경우
    # 예외 2 몬스터의 마지막 공격전에 체력이 0 이하가 된 경우
    
    for current_time in range(time+1):
        if health > max_health:
            health = max_health
        for attack_time, damage in attacks:
            if current_time == attack_time:
                health -= damage
                continue_success = 0
                break
        else:
            if health <= 0:
                return -1
            if health < max_health:
                health += heal_per_second
                if continue_success == casting_time:
                    health += plus_heal
                    continue_success = 0
                
        continue_success += 1
    
    if health <= 0:
        return -1
    return health