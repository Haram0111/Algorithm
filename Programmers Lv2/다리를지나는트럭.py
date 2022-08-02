from collections import deque

def solution(bridge_length, weight, truck_weights):
    On_bridge = deque()
    cnt = 0
    truck_weights = deque(truck_weights)
    sum_weights = 0
    while 1:
        cnt += 1
        if len(On_bridge) >= bridge_length: #들어가 있는 숫자의 개수가 브릿지의 길이보다 길면
            sum_weights -= On_bridge.popleft() #제일 처음 들어온 값을 내보낸다
        if sum_weights + truck_weights[0] <= weight: #만약 전체 합과 다음에 올라올 트럭의 무게의 합이 최대중량보다 작다면
            if len(truck_weights) == 1: #또한, 대기중인 트럭의 길이가 1이라면
                return cnt + bridge_length #마지막 것을 꺼내준다
            truck = truck_weights.popleft()
            On_bridge.append(truck) #대기중인 트럭의 길이가 1이 아니라면 그냥 꺼낸다
            sum_weights +=  truck
        else: #최대중량을 초과한다면
            On_bridge.append(0) #최대중량이라면