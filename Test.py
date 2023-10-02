def solution(inputString):
    n = len(inputString)
    middle = n//2
    
    firstHalf = inputString[:middle]
    secondHalf = inputString[middle:] if n % 2 == 0 else inputString[middle+1:]
    secondHalf = secondHalf[::-1]
    
    return True if firstHalf == secondHalf else False
    
    # hlbeeykoqqqqokyeeblh
    
if __name__ == "__main__":
    print (solution("aabaa"))