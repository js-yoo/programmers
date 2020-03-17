# https://programmers.co.kr/learn/courses/30/lessons/12910
# Difficulty : Level 1

# First_solution
def solution(arr,divisor):
    result=[]
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            result.append(arr[i])
    if not result:
        result.append(-1)
    return  sorted(result)

# Best_solution
def solution(arr,divisor):
    return  sorted([n for n in arr if n%divisor==0]) or [-1]

# Example)
# solution([5, 9, 7, 10],5) == [5, 10]
# solution([2, 36, 1, 3],1) == [1, 2, 3, 36]
# solution([3,2,6],10) == [-1]
