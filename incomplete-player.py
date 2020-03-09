# https://programmers.co.kr/learn/courses/30/lessons/42576
# Difficulty : Level 1

def solution(participant, completion):
    answer = ''
    count_dict={}
    for i in participant:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
        
    for i in completion:
        if i in count_dict:
            count_dict[i]-=1
    
    for name, count in count_dict.items():
        if count==1:
            answer=name
    
    return answer

# Example)
# solution(["leo", "kiki", "eden"], ["eden", "kiki"])
# >>> "leo"    
