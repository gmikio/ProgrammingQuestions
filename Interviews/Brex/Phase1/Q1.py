def solution(numbers):
    numberOfEven = 0
    
    for num in numbers:
        if num >= 10 and num < 100:
            numberOfEven += 1
        if num >= 1000 and num < 10000:
            numberOfEven += 1        
    
    return numberOfEven
    
