# https://programmers.co.kr/learn/courses/30/lessons/12916
# Difficulty : Level 1

def solution(s):
    return s.lower().count('p')==s.lower().count('y')

# Example)
# solution("pPoooyY") == true
# solution("Pyy") == false
