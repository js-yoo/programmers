# https://programmers.co.kr/learn/courses/30/lessons/12933
# Difficulty : Level 1

# 1) First_solution
def solution(n):
    a=sorted(int(i) for i in str(n))
    answer=0
    for k in range(len(a)):
        answer+=a[k]*(10**k)
    return answer

# 2) Frist_sketch
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)));
    
# Example)
# solution(118372) == 873211
