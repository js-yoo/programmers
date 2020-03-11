# https://programmers.co.kr/learn/courses/30/lessons/42840
# Difficulty : Level 1

def solution(answers):
    num=len(answers)
    one=[1,2,3,4,5]*2000
    two=[2,1,2,3,2,4,2,5]*1250
    three=[3,3,1,1,2,2,4,4,5,5]*1000
    count1,count2,count3=0,0,0
    maxcount=[]
    
    for c in range(0,num):
        
        if one[c]==answers[c]: 
            count1+=1
        if two[c]==answers[c]: 
            count2+=1
        if three[c]==answers[c]: 
            count3+=1
    maxcount=max((count1,count2,count3))
    result=[]
    
    if maxcount==count1: 
        result.append(1)
    if maxcount==count2: 
        result.append(2)
    if maxcount==count3: 
        result.append(3)
    
    return result

# Example)
# solution([1,2,3,4,5]) == [1]
# solution([1,3,2,4,2]) == [1,2,3]
