# https://programmers.co.kr/learn/courses/30/lessons/12937
# Difficulty : Level 1

1) First Solution
def solution(num):
    ans=["Even","Odd"]
    return ans[num%2]
    
# Example :
# solution(3) ==> "Odd"
# solution(4) ==> "Even"
