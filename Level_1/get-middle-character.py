# https://programmers.co.kr/learn/courses/30/lessons/12903
# Difficulty : Level 1

def solution(s):
    even="수"
    odd="박"
    answer=""
    for i in range(s):
        if i%2==0: #짝수(0,2,4,,,,)
            answer+=even
        else:
            answer+=odd
    return answer
    
# Example)
# solution("abcde") == "c"
# solution("qwer") == "we"
