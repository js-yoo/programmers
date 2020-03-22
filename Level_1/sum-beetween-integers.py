# https://programmers.co.kr/learn/courses/30/lessons/12912
# Difficulty : Level 1

def solution(a,b):
    if b<=a:
        a,b=b,a
    return sum(range(a,b+1))

# Example)
# solution(3,5) == 12
# solution(3,3) == 3
# solution(5,3) == 12
