# https://programmers.co.kr/learn/courses/30/lessons/12903
# Difficulty : Level 1

def solution(s):
    b=int(len(s)/2)
    return s[b-1]+s[b] if len(s)%2==0 else s[b]

# Example)
# solution("abcde") == "c"
# solution("qwer") == "we"
