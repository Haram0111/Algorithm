import math

def lcm(a,b):
  return (a * b) // math.gcd(a,b)

def solution(n, m):
    answer = []
    answer.append(math.gcd(n,m))
    answer.append(lcm(n,m)) #lcm이 3.9버전 이상에서만 가능
    return answer