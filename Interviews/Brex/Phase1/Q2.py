def solution(nums):
    def cyclicTShift(nums, t):
        return nums[t:] + nums[:t]
        
    def isSorted(lst):
        for i in range (1, len(lst)):
            if lst[i] < lst[i-1]:
                return False   
        return True 

    numberT = -1
    n = len(nums)
        
    for t in range (n):
        if isSorted(cyclicTShift(nums, t)):
            numberT = t         
    
    return numberT
