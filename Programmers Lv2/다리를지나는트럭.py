from collections import deque

def solution(bridge_length, weight, truck_weights):
    On_bridge = deque()
    cnt = 0
    sum_weights = 0
    truck_weights = deque(truck_weights)
    while(True):
        cnt += 1
        if len(On_bridge) != 0 and On_bridge[0][1] >= bridge_length:
            On_bridge.popleft()
            print(On_bridge)
        for i in range(len(On_bridge)):
            On_bridge[i][1] += 1
        if len(truck_weights) >= 1: #0 10
            wei = truck_weights[0]
            sum_weights += wei
            if sum_weights <= weight:
                On_bridge.append([wei,1])
            else:
                sum_weights -= wei
        if len(truck_weights) == 0:
            break
        # if len(On_bridge) == 0 and len(truck_weights) == 0:
        #     return cnt