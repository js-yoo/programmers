# https://programmers.co.kr/learn/courses/30/lessons/12922
# Difficulty : Level 1

# 1) First_solution
def solution(s):
    even="수"
    odd="박"
    answer=""
    for i in range(s):
        if i%2==0: 
            answer+=even
        else:
            answer+=odd
    return answer
    
# 2) not_my_solution
def water_melon(n):
    return ("수박"*n)[0:n]
    
# 3) not_my_solution
def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)

# Example)
# solution(3) == "수박수"
# solution(3) == "수박수박"

