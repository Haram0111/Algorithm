N = int(input())
lst = list(map(int,input().split(" ")))
start = 0
end = 1
partition = len(lst) - 1
#벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없다.
#즉 시작한 장소이외는 다 딸 수 있다
#그렇다면 시작하는 장소의 값이 낮을수록 좋다
#또한, 그전에 값이랑 비교해야한다
#partition이랑은 최대한 멀리 있는게 좋다