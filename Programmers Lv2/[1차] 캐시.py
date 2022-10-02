def solution(cacheSize, cities):
    lst = []
    time = 0
    if cacheSize == 0:
        return len(cities) * 5
    for i in range(len(cities)):
        city = cities[i].lower()
        if city in lst:
            lst.pop(lst.index(city))
            lst.append(city)
            time += 1            
        else:
            if len(lst) == cacheSize:
                lst.pop(0)
            lst.append(city)
            time += 5            
    return time