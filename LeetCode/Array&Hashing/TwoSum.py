from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
            
    for index, number in enumerate(nums):
        complement = target - number
        if complement in hashmap:
            return [hashmap[complement], index]
        hashmap[number] = index
        
    return []
                
def main():
    result = twoSum(nums = [2,7,11,15], target = 9)
    print (result)
    
if __name__ == "__main__":
    main()