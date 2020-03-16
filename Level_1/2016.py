# https://programmers.co.kr/learn/courses/30/lessons/12901
# Difficulty : Level 1

import datetime
def solution(a, b):
    return datetime.date(2016,a,b).strftime('%a').upper()

# Example) 
# solution(5,24) == "TUE"
