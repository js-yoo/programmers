# https://programmers.co.kr/learn/courses/30/lessons/12931
# Difficulty : Level 1

# 1) First_solution
def solution(s):
    s=str(s)
    result = 0
    for i in range(len(s)):
        result += int(s[i])
    return result

# 2) Second_solution
def solution(n):
    return sum([int(i) for i in str(n)])

# Example)
# solution(123) == 6
# solution(987) == 24
