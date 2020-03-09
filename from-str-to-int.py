# https://programmers.co.kr/learn/courses/30/lessons/12925
# Difficulty : Level 1

# 1) First_solution
def solution(s):
    return int(s) if s.isdigit() or '+' in s else 0-int(s[1:])
    
# 2) Shortest_silution
def solution(s):
    return int(s)
    
# Example)
# solution("1234") == 1234
# solution("-1234") == 1234
