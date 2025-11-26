from collections import deque
def solution(bandage, health, attacks):     # t: 시전 시간, x: 초당 회복량, y: 추가 회복량 health: 최대 체력
    t, x, y = bandage[0], bandage[1], bandage[2]
    remain_health = health
    
    attack_time = []
    damages = []
    for time, damage in attacks:
        attack_time.append(time)
        damages.insert(0, damage)
        
    attack_cnt = 0
    for i in range(1, attack_time[-1] + 1):
        if i not in attack_time:
            remain_health += x
            attack_cnt += 1
            if attack_cnt == t:
                remain_health += y
                attack_cnt = 0
            if remain_health > health:
                remain_health = health
        else:
            damage = damages.pop()
            remain_health -= damage
            if remain_health <= 0:
                return -1
            attack_cnt = 0
             
    return remain_health